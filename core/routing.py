import flet as ft
from src import HomeView
from src import Camera


class Routing:
    def __init__(self, page: ft.Page):
        self.page = page

    def route_change(self):
        self.page.views.clear()
        home_ui = HomeView(self.page)
        self.page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.SafeArea(
                        width=800,
                        align=ft.Alignment.CENTER,
                        content=ft.Column(
                            controls=[
                                home_ui.header,
                                home_ui.content
                            ]
                        ),
                        expand=True
                    )
                ],
            )
        )
        if self.page.route == "/camera":
            camera_ui = Camera(self.page)
            self.page.views.append(
                ft.View(
                    route="/camera",
                    controls=[
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    camera_ui.panel
                                ]
                            ),
                            expand=True
                        )
                    ],
                )
            )
        self.page.update()

    async def view_pop(self, e):
        if e.view is not None:
            self.page.views.remove(e.view)
            top_view = self.page.views[-1]
            await self.page.push_route(top_view.route)