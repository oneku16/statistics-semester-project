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
from app.src.database import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def signup_view(page: Page, switch_view, login_view):
    def handle_signup(e):
        db = SessionLocal()
        if get_user_by_email(db, email.value):
            page.snack_bar = SnackBar(Text("Email already exists."), bgcolor="red")
        else:
            hashed_password = pwd_context.hash(password.value)
            create_user(db, username.value, email.value, hashed_password)
            page.snack_bar = SnackBar(Text("Signup successful!"))
            switch_view(login_view)
        db.close()
        page.snack_bar.open = True
        page.update()

    username = TextField(label="Username", width=300)
    email = TextField(label="Email", width=300)
    password = TextField(label="Password", password=True, width=300)
    signup_button = ElevatedButton("Sign Up", on_click=handle_signup)
    back_button = ElevatedButton("Back to Login", on_click=lambda _: switch_view(login_view))

    return Column(
        controls=[
            Text(
                value="Sign Up",
                size=24,
                weight=FontWeight.BOLD,
            ),
            username,
            email,
            password,
            Row(
                controls=[
                    signup_button,
                    back_button,
                ],
                alignment=MainAxisAlignment.CENTER)
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
