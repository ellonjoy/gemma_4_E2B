import flet as ft
import base64
from core import state

class AddBtn(ft.Container):
    def __init__(self):
        """
        Membuat tampilan UI tombol + secara dinamis yang akan otomatis
        berubah saat trigger di global state di update.
        """

        super().__init__()
        ############### Mendeklarasikan tampilan semula ####################
        self._content = ft.Column(
            controls=[
                ft.PopupMenuButton(
                    icon=ft.Icons.ADD,
                    items=[
                        ft.PopupMenuItem(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.IMAGE),
                                    ft.Text("Gambar")
                                ]
                            )
                        ),
                        ft.PopupMenuItem(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.ADD_A_PHOTO),
                                    ft.Text("Kamera")
                                ]
                            ),
                            on_click=...
                        ),
                    ],
                    width=40,
                    height=40,
                    margin=ft.Margin(bottom=4),
                    visible=True
                ),
                ft.Stack(
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src=base64.b64decode(
                                    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wIAAgMBAp0YVwAAAABJRU5ErkJggg=="
                                ),
                                fit=ft.BoxFit.COVER,
                                border_radius=8
                            ),
                            width=40,
                            height=40,
                            border_radius=8
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_size=12,
                            width=20,
                            right=1,
                            top=-15,
                            mouse_cursor=ft.MouseCursor.CLICK,
                        )
                    ],
                    visible=False
                )
            ]
        )

        ################### Mendefinisikan tampilan ####################
        self.content = self._content
        self.width = 40
        self.height = 40
        self.margin = ft.Margin(bottom=4)

    def did_mount(self):
        self.page.pubsub.subscribe(self.update_ui_btn)

    def will_unmount(self):
        self.page.pubsub.unsubscribe_all()

    def update_ui_btn(self, message) -> None:
        """
        Melakukan update tampilan UI add_btn ketika ada data gambar yang diupload.
        """

        if state.img_bytes:
            self.content.controls[0].visible = False
            self.content.controls[1].controls[0].content.src = state.img_bytes
            self.content.controls[1].visible = True
        else:
            self.content.controls[0].visible = True
            self.content.controls[1].visible = False
        self.update()