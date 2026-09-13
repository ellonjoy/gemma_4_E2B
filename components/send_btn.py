import flet as ft
import asyncio
from controllers import start_inference
from core import state


class SendBtn(ft.Container):
    def __init__(self):
        """
        Membuat tampilan prompt input secara dinamis ketika ada trigger.
        """
        
        super().__init__()
        self._content: ft.IconButton = ft.IconButton(
            icon=ft.Icons.ARROW_UPWARD,
            icon_size=18,
            icon_color="#ffffff"
        )
        self._gradient = ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=[
                ft.Colors.BLUE,
                ft.Colors.PINK
            ]
        )
        self.animted_gradient = False

        self.content = self._content
        self.gradient = self._gradient
        self.border_radius = 50
        self.width = 40
        self.height = 40
        self.margin = ft.Margin(bottom=4)
        self.animate = ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT)

    def did_mount(self):
        self.page.pubsub.subscribe(self.update_ui_btn)

    def will_unmount(self):
        self.page.pubsub.unsubscribe_all()

    async def update_ui_btn(self, message):
        if state.inference:
            self.animted_gradient = True
            self.content.icon = ft.Icons.SQUARE
            while self.animted_gradient:
                self.gradient.begin = ft.Alignment.TOP_CENTER
                self.gradient.end = ft.Alignment.BOTTOM_CENTER
                self.update()
                await asyncio.sleep(.2)

                self.gradient.begin = ft.Alignment.TOP_RIGHT
                self.gradient.end = ft.Alignment.BOTTOM_LEFT
                self.update()
                await asyncio.sleep(.2)

                self.gradient.begin = ft.Alignment.CENTER_RIGHT
                self.gradient.end = ft.Alignment.CENTER_LEFT
                self.update()
                await asyncio.sleep(.2)

                self.gradient.begin = ft.Alignment.BOTTOM_RIGHT
                self.gradient.end = ft.Alignment.TOP_LEFT
                self.update()
                await asyncio.sleep(.2)

                self.gradient.begin = ft.Alignment.BOTTOM_CENTER
                self.gradient.end = ft.Alignment.TOP_CENTER
                self.update()
                await asyncio.sleep(.2)

                self.gradient.begin = ft.Alignment.BOTTOM_LEFT
                self.gradient.end = ft.Alignment.TOP_RIGHT
                self.update()
                await asyncio.sleep(.2)

                self.gradient.begin = ft.Alignment.CENTER_LEFT
                self.gradient.end = ft.Alignment.CENTER_RIGHT
                self.update()
                await asyncio.sleep(.2)

                self.gradient.begin = ft.Alignment.TOP_LEFT
                self.gradient.end = ft.Alignment.BOTTOM_RIGHT
                self.update()
                await asyncio.sleep(.2)
                
        else:
            self.animted_gradient = False
            self.content.icon = ft.Icons.ARROW_UPWARD
            self.update()