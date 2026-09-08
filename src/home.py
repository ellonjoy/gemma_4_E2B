import flet as ft
from components import ListViewChats


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
                ft.TextButton(
                    content="AI Assistent",
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            size=25,
                            weight="bold"
                        ),
                        color="#ffffff",
                    ),
                    on_click=...
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
        self.panel_input_row = ft.Row(
            controls=[],
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