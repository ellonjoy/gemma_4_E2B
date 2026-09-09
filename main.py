import flet as ft
import litert_lm as llm
from core import state
from core import Routing


with llm.Engine(
    state.model_path,
    backend=llm.Backend.CPU(),
    vision_backend=llm.Backend.CPU()
) as engine:
    def main(page: ft.Page):
        routing = Routing(page)
        state.engine = engine
        state.conversation = engine.create_conversation()

        page.on_route_change = routing.route_change
        page.on_view_pop = routing.view_pop
        
        routing.route_change()

    if __name__=="__main__":
        ft.run(main)