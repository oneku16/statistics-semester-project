import flet as ft
from flet import Page, TextField, ElevatedButton, Column, Row, Text, Container, padding, alignment
from db.database import SessionLocal, init_db
from db.crud import create_user, get_user_by_email
from passlib.context import CryptContext
from sqlalchemy.orm import Session

# Initialize the database (run this once)
init_db()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Function to handle authentication
def authenticate_user(email, password, db):
    user = get_user_by_email(db, email)
    if user and pwd_context.verify(password, user.password_hash):
        return user
    return None


# Main App
def main(page: Page):
    page.title = "Statistic Calculator"
    page.padding = padding.all(20)
    page.update()

    # Helper function to switch views
    def switch_view(view):
        page.clean()
        page.add(view)
        page.update()

    # Initial views
    def login_view():
        def handle_login(e):
            db = SessionLocal()
            user = authenticate_user(email.value, password.value, db)
            db.close()
            if user:
                page.snack_bar = ft.SnackBar(ft.Text("Login successful!"))
                switch_view(main_page_view())
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Invalid email or password."), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        email = TextField(label="Email", width=300)
        password = TextField(label="Password", password=True, width=300)
        login_button = ElevatedButton("Log In", on_click=handle_login)
        signup_button = ElevatedButton("Sign Up", on_click=lambda _: switch_view(signup_view()))

        return Column([
            Text(
                value="Login",
                size=24,
                weight="bold",
            ),
            email,
            password,
            Row(
                [
                        login_button,
                        signup_button
                ],
                alignment="center",
            )
        ],
            alignment="center",
            horizontal_alignment="center",
        )

    def signup_view():
        def handle_signup(e):
            db = SessionLocal()
            if get_user_by_email(db, email.value):
                page.snack_bar = ft.SnackBar(ft.Text("Email already exists."), bgcolor="red")
            else:
                hashed_password = pwd_context.hash(password.value)
                create_user(db, username.value, email.value, hashed_password)
                page.snack_bar = ft.SnackBar(ft.Text("Signup successful!"))
                switch_view(login_view())
            db.close()
            page.snack_bar.open = True
            page.update()

        username = TextField(
            label="Username",
            width=300,
        )
        email = TextField(
            label="Email",
            width=300,
        )
        password = TextField(
            label="Password",
            password=True,
            width=300,
        )
        signup_button = ElevatedButton(
            text="Sign Up",
            on_click=handle_signup,
        )
        back_button = ElevatedButton(
            text="Back to Login",
            on_click=lambda _: switch_view(login_view()))

        return Column(
            controls=[
                    Text(
                        value="Sign Up",
                        size=24,
                        weight="bold",
                    ),
                    username,
                    email,
                    password,
                    Row(
                        controls=[
                                signup_button,
                                back_button,
                        ],
                        alignment="center",
                    )
            ],
            alignment="center",
            horizontal_alignment="center",
        )

    def main_page_view():
        return Column([
            Text("Main Page", size=24, weight="bold"),
            Text("This page is currently empty.")
        ], alignment="center", horizontal_alignment="center")

    switch_view(login_view())


# Run the app
ft.app(target=main)
