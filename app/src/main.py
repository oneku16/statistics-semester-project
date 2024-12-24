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


    page.clean()
    page.add(
        LoginReturn(page=page)
    )
    page.update()


if __name__ == "__main__":
    init_db()
    ft.app(target=main)
