import flet as ft
import asyncio
from core import state

class ListViewChats(ft.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.padding = 12
        self.auto_scroll = True
        # self.stop = True
        self.scroll = ft.ScrollMode.HIDDEN
        self.controls = state.chats

    def did_mount(self):
        self.page.pubsub.subscribe(self.update_ui_chats)

    def will_unmount(self):
        self.page.pubsub.unsubscribe_all()

    async def update_ui_chats(self, message):
        if state.inference:
            self.stop = False
            # self.controls.extend(state.chats)

            while not self.stop:
                self.update()
                await asyncio.sleep(.01)
        else:
            self.stop = True
            self.update()

        if message == "new_conversation":
            self.controls = state.chats
            self.update()