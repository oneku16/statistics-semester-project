import flet as ft
from app.src.views.login import login_view
from app.src.views.signup import signup_view
from app.src.views.calculator import calculator
from app.src.database import init_db

from app.src.components.login_components import LoginReturn


def main(page: ft.Page):
    page.title = "Statistic Calculator"
    page.padding = ft.padding.all(20)
    page.update()

    def switch_view(view_func):
        page.clean()
        page.add(view_func(page, switch_view, calculator, signup_view, login_view))
        page.update()
    page.client_storage.clear()
    if page.client_storage.contains_key(key="user_id"):
        page.clean()
        page.add(
            calculator(
                page=page,
                switch_view=switch_view,
                login_view=login_view,
            )
        )
        page.update()

    else:
        page.clean()
        page.add(
            LoginReturn(page=page)
        )
        page.update()


if __name__ == "__main__":
    init_db()
    ft.app(target=main)
