from flet import Page

from db.database import init_db, SessionLocal
from db.crud import create_user, get_user_by_email


def main(page: Page):
    ...


if __name__ == "__main__":
    init_db()
    db = SessionLocal()

