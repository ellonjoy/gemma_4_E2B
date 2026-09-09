import flet as ft
from core import state

class ListViewChats(ft.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.padding = 12
        self.auto_scroll = True
        self.stop = True
        self.controls = state.chats

    def did_mount(self):
        self.page.pubsub.subscribe(self.update_ui_chats)

    def will_unmount(self):
        self.page.pubsub.unsubscribe_all()

    def update_ui_chats(self, message):
        if state.inference:
            self.stop = False

            while not self.stop:
                self.update()
        else:
            self.stop = True
            self.update()

        if message == "new_conversation":
            self.controls = state.chats
            self.update()