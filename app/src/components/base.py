from passlib.context import CryptContext

from app.src.database import SessionLocal


class DB:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class WithDB(DB):
    _db = None

    @property
    def db(self) -> SessionLocal:
        if self._db is None:
            self._db = SessionLocal()
        return self._db

    def close_db(self) -> None:
        self.db.close()
        self._db = None
