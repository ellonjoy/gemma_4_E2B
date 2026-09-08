import flet as ft
from src import HomeView


class Routing:
    def __init__(self, page: ft.Page):
        self.page = page
        self.home_ui = HomeView(self.page)

    def route_change(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.SafeArea(
                        content=ft.Column(
                            controls=[
                                self.home_ui.header,
                                self.home_ui.content
                            ]
                        ),
                        expand=True
                    )
                ],
            )
        )
        if self.page.route == "/camera":
            self.page.views.append(
                ft.View(
                    route="/camera",
                    controls=[
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    # camera_ui.panel
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