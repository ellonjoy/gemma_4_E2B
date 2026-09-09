import flet as ft


async def add_picture():
    file = await ft.FilePicker().pick_files(
        dialog_title="Picture",
        allow_multiple=False,
        allowed_extensions=["jpg", "jpeg", "png"],
        with_data=True
    )
    if file:
        return file[0].bytes