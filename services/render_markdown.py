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
            controls.extend(process_text_and_table(text_before))

        controls.append(create_custom_block_code(lang_code, content))
        last_end = end
    text_end = md_text[last_end:]
    if text_end:
        controls.extend(process_text_and_table(text_end))

    return ft.Column(
        controls=controls
    )

def process_text_and_table(md_text: str):
    controls = []
    table_pattern = r"((?:^[^\n]*\|[^\n]*$\n?)+)"

    for part in re.split(table_pattern, md_text, flags=re.MULTILINE):
        if not part.strip():
            continue

        if "|" in part and "\n" in part.strip():
            controls.append(create_custom_block_table(part))
        else:
            controls.append(ft.Markdown(
                value=part.strip(),
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                code_theme=ft.MarkdownCodeTheme.TOMORROW_NIGHT_BRIGHT,
                soft_line_break=True
            ))

    return controls

def create_custom_block_code(language: str, content_text: str) -> ft.Container:
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

def create_custom_block_table(md_text: str):
    lines = md_text.strip().split("\n")
    if not lines:
        return ft.Text("")

    headers = [col.strip() for col in lines[0].split("|") if col.strip()]
    if not headers:
        return ft.Text(lines[0])

    row_data = []
    if len(lines) > 2:
        for line in lines[2:]:
            if line.strip() == "":
                continue

            cells = [cell.strip() for cell in line.split("|") if cell.strip()]
            cells = cells + [""] * (len(headers)-len(cells))
            cells = cells[:len(headers)]
            row_data.append(cells)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.DataTable(
                            horizontal_lines=ft.BorderSide(1, ft.Colors.OUTLINE_VARIANT),
                            columns=[
                                ft.DataColumn(
                                    ft.Text(
                                        value=h,
                                        weight="bold"
                                    )
                                ) for h in headers
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(
                                            ft.Text(
                                                value=c
                                            )
                                        ) for c in row
                                    ]
                                ) for row in row_data
                            ]
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )