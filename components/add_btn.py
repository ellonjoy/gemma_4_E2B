import flet as ft

class AddBtn(ft.Container):
    def __init__(self):
        """
        Membuat tampilan UI tombol + secara dinamis yang akan otomatis
        berubah saat trigger di global state di update.
        """

        super().__init__()
        ############### Mendeklarasikan tampilan semula ####################
        self._content: ft.PopupMenuButton = ft.PopupMenuButton(
            icon=ft.Icons.ADD,
            items=[
                ft.PopupMenuItem(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.IMAGE),
                            ft.Text("Gambar")
                        ]
                    ),
                    on_click=...
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
            ]
        )

        ################### Mendefinisikan tampilan ####################
        self.content = self._content
        self.width = 40
        self.height = 40
        self.margin = ft.Margin(bottom=4)