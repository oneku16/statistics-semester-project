from flet import (
    Column,
    Text,
    ElevatedButton
)
from flet.core.types import (
    CrossAxisAlignment,
    FontWeight,
    MainAxisAlignment,
)


def calculator(page):
    username = page.client_storage.get("username", "Unknown User")

    def handle_logout(e):
        page.client_storage.remove("user_id")
        page.client_storage.remove("username")
        switch_view(login_view)

    return Column(
        controls=[
            Text(
                value=f"Welcome, {username}!",
                size=24,
                weight=FontWeight.BOLD),
            Text(
                value="This is the main page.",
            ),
            ElevatedButton(
                text="Log Out",
                on_click=handle_logout,)
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER)
