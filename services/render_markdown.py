import flet as ft
import re

def render(md_text: str) -> ft.Column:
    """
    Melakukan rendering markdown dari teks respon yang dihasilkan model dalam bentuk markdown.
    Argumen berupa potongan teks yang akan diolah dan nantinya
    akan mengembalikan property 'ft.Column'.
    """

    if md_text.count("```") % 2 != 0:
        md_text += "\n```"

    controls = []
    pattern = r"```(\w*)\n(.*?)```"
    last_end = 0

    for match in re.finditer(pattern, md_text, re.DOTALL):
        start, end = match.span()
        lang_code = match.group(1)
        content = match.group(2)

        text_before = md_text[last_end:start]
        if text_before:
            controls.append(ft.Markdown(
                value=text_before,
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                code_theme=ft.MarkdownCodeTheme.TOMORROW_NIGHT_BRIGHT,
                soft_line_break=True
            ))

        controls.append(create_custom_block(lang_code, content))
        last_end = end
    text_end = md_text[last_end:]
    if text_end:
        controls.append(ft.Markdown(
            value=text_end,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            code_theme=ft.MarkdownCodeTheme.TOMORROW_NIGHT_BRIGHT,
            soft_line_break=True
        ))
    return ft.Column(
        controls=controls
    )

def create_custom_block(language: str, content_text: str) -> ft.Container:
    """
    Membuat custom block kode ketika model menghasilkan sebuah block kode saat
    melakukan respon yang ditanda dengan ```block code``` dan mengembalikan property
    'ft.Container'.
    """
    async def copy_text(e):
        await ft.Clipboard().set(content_text)

    custom_block_col = ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            value=language if language else "Bash",
                            size=15,
                            margin=ft.Margin(left=6),
                            weight="bold",
                            color=ft.Colors.GREY_400
                        ),
                        ft.IconButton(
                            icon=ft.Icons.COPY,
                            on_click=copy_text,
                            icon_size=18,
                            tooltip=ft.Tooltip(message="Copy")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                padding=2
            ),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Markdown(
                            value=f"```{language}\n{content_text}\n```",
                            selectable=True,
                            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                            code_theme=ft.MarkdownCodeTheme.TOMORROW_NIGHT_BRIGHT,
                            soft_line_break=True
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO
                )
            )
        ]
    )
    custom_block = ft.Container(
        content=custom_block_col,
        bgcolor="#1e1e1e",
        border_radius=15
    )

    return custom_block