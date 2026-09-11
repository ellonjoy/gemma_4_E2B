import flet as ft
import asyncio
from core import state
from services import create_conversation_model
from services import inferance
from services import add_picture
from services import render
from services import get_camera
from services import init_camera
from services import take_a_photo


async def new_conversation(page: ft.Page) -> None:
    """
    Membuat konversasi baru saat context window telah mencapai limit.
    Fungsi new_conversation berfungsi untuk membuat konteks percakapan baru dengan memperbarui nilai state.conversation.

    ## **Args**:
        - **(page)** -> Referensi page yang dibutuhkan untuk melakukan broadcast update ke UI tertentu.
    """

    state.conversation = create_conversation_model(state.engine, state.initial_message)
    state.chats = []
    page.pubsub.send_all("new_conversation")

async def start_inference(page: ft.Page, prompt: str) -> None:
    """
    # **Deskripsi**

    Model melakukan inference terhadap prompt input seperti teks atau gambar.
    Fungsi ini akan mengubah nilai API state agar UI dapat melakukan update saat fungsi ini dipanggil.
    Fungsi generator seperti inference() akan menghasilkan chunk teks dan diproses didalam looping kemudian
    akan diteruskan ke fungsi render() untuk melakukan rendering markdown.

    ## **Args**:
        - **(page)** -> Referensi page yang dibutuhkan untuk melakukan broadcast update ke UI tertentu.
        - **(prompt)** -> Berupa teks yang akan dijadikan sebagai inputan untuk melakukan inference.
    """

    if prompt == "":
        return

    state.chats = []
    state.inference = True
    page.pubsub.send_all("true")
    prompt_text = ft.Container(
        content=ft.Container(
            content=ft.Text(
                value=prompt,
                expand_loose=True
            ),
            bgcolor=ft.Colors.BLUE,
            padding=15,
            expand_loose=True,
            border_radius=12,
        ),
        alignment=ft.Alignment.CENTER_RIGHT,
        margin=ft.Margin(bottom=12)
    )
    response_text = ft.Container(
        margin=ft.Margin(bottom=12)
    )
    if state.img_bytes is not None:
        prompt_image = ft.Container(
            content=ft.Container(
                content=ft.Image(
                    src=state.img_bytes,
                    fit=ft.BoxFit.COVER,
                    border_radius=14
                ),
                border=ft.Border.all(2, ft.Colors.BLUE),
                border_radius=14,
                width=200,
                height=200
            ),
            alignment=ft.Alignment.CENTER_RIGHT,
            margin=ft.Margin(bottom=5)
        )
        state.chats.append(prompt_image)
    state.chats.append(prompt_text)
    state.chats.append(response_text)
    stream = inferance(state.conversation, prompt.strip(), state.img_bytes) # Fungsi generator
    state.img_bytes = None
    await asyncio.sleep(.2)
    async for chunk in stream:
        response_text.content = render(chunk)
    state.inference = False
    page.pubsub.send_all("false")

async def add_image(page: ft.Page) -> None:
    """
    Memanggil fungsi add_picture() untuk menambahkan gambar dan mengupdate nilai API state.img_bytes.

    ## **Args**:
        - **(page)** -> Referensi page yang dibutuhkan untuk melakukan broadcast update ke UI tertentu.
    """

    state.img_bytes = await add_picture()
    page.pubsub.send_all("add_picture")

async def del_image(page: ft.Page) -> None:
    """
    Menghapus nilai gambar dari API state dan update UI tertentu.

    ## **Args**:
        - **(page)** -> Referensi page yang dibutuhkan untuk melakukan broadcast update ke UI tertentu.
    """

    state.img_bytes = None
    page.pubsub.send_all("del_picture")

async def open_cam(page: ft.Page) -> None:
    """
    # **Deskripsi**

    UI berpindah ke halaman tampilan camera dan memanggil fungsi asyncrhonous get_camera()
    untuk mengambil jumlah kamera perangkat yang tersedia dan init_camera() untuk melakukan
    inisialisasi terhadap kamera yang dipilih.

    ## **Args**:
        - **(page)** -> Referensi page yang dibutuhkan untuk melakukan broadcast update ke UI tertentu.
    """

    await page.push_route("/camera")
    try:
        await get_camera(state.camera)
    except RuntimeError:
        await page.push_route("/")
    await init_camera(state.camera)

async def take_picture(e: ft.ControlEvent):
    """
    Memanggil fungsi take_a_photo() untuk mengambil foto dan mengupdate nilai API state.img_bytes
    dan otomatis berpindah ke halaman utama.

    ## **Args**:
        - **(e)** -> Event Control.
    """

    state.img_bytes = await take_a_photo(state.camera)
    await e.page.push_route("/")
    e.page.pubsub.send_all("add_picture")