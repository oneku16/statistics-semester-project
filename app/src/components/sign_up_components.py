from flet import (
    Column,
    ElevatedButton,
    TextField,
    Text,
    SnackBar,
    Row,
    Page
)
from flet.core.types import (
    CrossAxisAlignment,
    FontWeight,
    MainAxisAlignment,
)

from app.src.crud.user_crud import get_user_by_email, create_user
from app.src.utils import switch_view
from app.src.components.base import WithDB




class SignUp(WithDB, Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.username = TextField(label="Username", width=300)
        self.email = TextField(label="Email", width=300)
        self.password = TextField(label="Password", password=True, width=300)
        self.signup_button = ElevatedButton("Sign Up", on_click=self.handle_signup)
        self.back_button = ElevatedButton("Back to Login", on_click=self.handle_back)
        self.controls = [
            Text(
                value="Sign Up",
                size=24,
                weight=FontWeight.BOLD,
            ),
            self.username,
            self.email,
            self.password,
            Row(
                controls=[
                    self.signup_button,
                    self.back_button,
                ],
                alignment=MainAxisAlignment.START)
        ]
        self.alignment = MainAxisAlignment.START
        self.horizontal_alignment = CrossAxisAlignment.START

    def handle_signup(self, event):
        if get_user_by_email(self.db, self.email.value):
            self.page.snack_bar = SnackBar(Text("Email already exists."), bgcolor="red")
        else:
            create_user(self.db, self.username.value, self.email.value, self.password.value)
            self.page.snack_bar = SnackBar(Text("Signup successful!"))
            from app.src.components.login_components import LoginReturn
            switch_view(page=self.page, control=LoginReturn(self.page))

        self.close_db()
        self.page.snack_bar.open = True
        self.page.update()

    def handle_back(self, event):
        from app.src.components.login_components import LoginReturn
        switch_view(page=self.page, control=LoginReturn(self.page))
        self.page.snack_bar.open = True
        self.page.update()
