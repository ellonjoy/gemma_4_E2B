import flet as ft
import asyncio
from controllers import start_inference, new_conversation, add_image, del_image, open_cam
from components import ListViewChats
from components import AddBtn
from components import PromptInput
from components import SendBtn


class HomeView:
    def __init__(self, page: ft.Page) -> None:
        """
        Membuat tampilan halaman utama chatbot yang terdiri dari:\n
        - Header: Tampilan paling atas yang berisi 'TextButton'.
        - Content: Tampilan body halaman yang terdiri dari:
        """

        ##################### Referensi halaman ###########################
        self.page = page

        ######################## Header ########################
        self.header_row = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.TextButton(
                            content="SUBYANTO",
                            style=ft.ButtonStyle(
                                text_style=ft.TextStyle(
                                    size=25,
                                    weight="bold"
                                ),
                                padding=0,
                                color="#ffffff",
                            ),
                            on_click=lambda e: asyncio.create_task(new_conversation(self.page))
                        ),
                        ft.Text(
                            value="Chatbot offline omon-omon",
                            size=15
                        )
                    ]
                ),
                ft.Container(expand=True)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        self.header = ft.Container(
            content=self.header_row,
            padding=ft.Padding(
                top=15,
                bottom=15
            )
        )

        ###################### Content ###########################
        self.lv_chats = ListViewChats()
        self.add_btn = AddBtn()
        self.prompt_input = PromptInput()
        self.send_btn = SendBtn()
        self.add_btn.content.controls[0].items[0].on_click = lambda e: asyncio.create_task(add_image(self.page))
        self.add_btn.content.controls[0].items[1].on_click = lambda e: asyncio.create_task(open_cam(self.page))
        self.add_btn.content.controls[1].controls[1].on_click = lambda e: asyncio.create_task(del_image(self.page))
        self.prompt_input.on_submit = lambda e: asyncio.create_task(start_inference(self.page, self.prompt_input.value))
        self.send_btn.content.on_click = lambda e: asyncio.create_task(start_inference(self.page, self.prompt_input.value))

        self.panel_input_row = ft.Row(
            controls=[
                self.add_btn,
                self.prompt_input,
                self.send_btn
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=0,
            vertical_alignment=ft.MainAxisAlignment.END,
        )
        self.panel_input = ft.Container(
            content=self.panel_input_row,
            bgcolor="#1b1b1b",
            border=ft.Border.all(1, "#2c2b2b"),
            padding=4,
            border_radius=20,
            margin=10
        )
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    self.lv_chats,
                    self.panel_input
                ],
                expand=True
            ),
            expand=True
        )