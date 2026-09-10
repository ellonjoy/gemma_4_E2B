import flet as ft
import asyncio
from core import state
from controllers import take_picture

class Camera:
    def __init__(self, page: ft.Page):
        self.page = page
        self.take_btn = ft.Container(
            content=ft.IconButton(
                icon=ft.Icons.CAMERA_ALT,
                icon_color="#1B1B1B",
                on_click=take_picture
            ),
            width=45,
            height=45,
            bgcolor="#ebe6e6",
            border_radius=50,
            bottom=20,
            on_click=lambda e: asyncio.create_task(take_picture(e))
        )
        self.panel = ft.Container(
            content=ft.Stack(
                controls=[
                    state.camera,
                    self.take_btn
                ],
                expand=True,
                alignment=ft.Alignment.CENTER
            ),
            expand=True,
            alignment=ft.Alignment.CENTER
        )