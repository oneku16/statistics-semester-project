from flet import (
    Page,
    TextField,
)
from app.src.components.login_components import LoginReturn


def login_view(page: Page):
    email_username = TextField(label="Email or Username", width=300)
    password = TextField(label="Password", password=True, width=300)
    login_return = LoginReturn(
        page=page,
        email_username=email_username,
        password=password,
    )
    return login_return
