import flet as ft
import gc
import litert_lm as llm
from core import state
from core import Routing

with llm.Engine(
    state.model_path,
    max_num_tokens=8192,
    backend=llm.Backend.CPU(),
    vision_backend=llm.Backend.CPU()
) as engine:
    def main(page: ft.Page):
        routing = Routing(page)
        state.engine = engine
        state.conversation = engine.create_conversation(messages=state.initial_message)

        page.on_route_change = routing.route_change
        page.on_view_pop = routing.view_pop
        
        routing.route_change()

    if __name__=="__main__":
        try:
            ft.run(main)
        except KeyboardInterrupt:
            print("berhenti")
        finally:
            if state.conversation:
                del state.conversation
            if state.engine:
                del state.engine
            gc.collect()
            gc.collect()