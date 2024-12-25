from flet import (
    Page,
    Column,
    ElevatedButton,
    TextField,
    Text,
    SnackBar,
    Row,
)

from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment

from app.src.crud.user_crud import get_user_by_email, get_user_by_username
from app.src.components.base import WithDB
from app.src.utils import switch_view


class LoginReturn(WithDB, Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.email_username = TextField(value="a@a.a", label="Email or Username", width=300)
        self.password = TextField(value="a", label="Password", password=True, width=300)
        self.alignment = MainAxisAlignment.CENTER,
        self.horizontal_alignment = CrossAxisAlignment.CENTER,
        self.controls=[
            Text(
                value="Login",
                size=24,
                weight=FontWeight.BOLD,
            ),
            self.email_username,
            self.password,
            Row(
                controls=[
                    ElevatedButton(
                        text="Log In",
                        on_click=self.handle_login,
                    ),
                    ElevatedButton(
                        text="Sign Up",
                        on_click=self.handle_signup,
                    ),
                ],
            )
        ]

    def handle_login(self, event):
        from app.src.components.calculator_components import CalculatorHandler as LocalCalculatorComponent
        if '@' in self.email_username.value:
            user_instance = get_user_by_email(self.db, self.email_username.value)
        else:
            user_instance = get_user_by_username(self.db, self.email_username.value)
        if user_instance and self.password.value == user_instance.password_hash:
            self.page.client_storage.set("user_id", user_instance.user_id)
            self.page.client_storage.set("username", user_instance.username)
            self.page.snack_bar = SnackBar(Text("Login successful!"))

            switch_view(page=self.page, control=LocalCalculatorComponent(page=self.page))
        else:
            self.page.snack_bar = SnackBar(Text("Invalid credentials"), bgcolor="red")
        self.page.snack_bar.open = True
        self.page.update()

    def handle_signup(self, event):
        from app.src.components.sign_up_components import SignUp
        switch_view(page=self.page, control=SignUp(page=self.page))
