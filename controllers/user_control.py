import flet as ft
import asyncio
from core import state
from services import inferance


async def start_inference(page: ft.Page, prompt: str):
    page.pubsub.send_all("true")
    prompt_text = ft.Container(
        content=ft.Container(
            content=ft.Text(
                value=prompt,
                expand_loose=True
            ),
            bgcolor=ft.Colors.BLUE,
            padding=15,
            expand_loose=True,
            border_radius=12,
        ),
        alignment=ft.Alignment.CENTER_RIGHT,
        margin=ft.Margin(bottom=12)
    )
    response_text = ft.Container(
        margin=ft.Margin(bottom=12)
    )
    state.chats.append(prompt_text)
    state.chats.append(response_text)
    async for chunk in inferance(state.conversation, prompt.strip()):
        response_text.content = ft.Markdown(value=chunk)
    page.pubsub.send_all("false")