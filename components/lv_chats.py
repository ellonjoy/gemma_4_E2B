import flet as ft

class ListViewChats(ft.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.padding = 12
        self.auto_scroll = True