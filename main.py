import flet as ft
from core import Routing

def main(page: ft.Page):
    routing = Routing(page)

    page.on_route_change = routing.route_change
    page.on_view_pop = routing.view_pop
    
    routing.route_change()

if __name__=="__main__":
    ft.run(main)