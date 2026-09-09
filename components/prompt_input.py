import flet as ft


class PromptInput(ft.TextField):
    def __init__(self):
        """
        Membuat tampilan prompt input secara dinamis ketika ada trigger.
        """

        super().__init__()
        self.hint_text = "Ada yang ingin anda tanyakan?"
        self.multiline = True
        self.max_lines = 5
        self.content_padding = 0
        self.text_size = 13
        self.hint_style = ft.TextStyle(
            color="#525252"
        )
        self.shift_enter = True
        self.expand = True
        self.on_focus = True
        self.border_color = "transparent"
        self.focused_border_color = "transparent"

    def did_mount(self):
        self.page.pubsub.subscribe(self.update_ui_input)

    def will_unmount(self):
        self.page.pubsub.unsubscribe_all()

    def update_ui_input(self, message):
        self.value = ""
        self.update()