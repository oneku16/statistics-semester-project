from flet import (
    Page,
    Column,
    ElevatedButton,
    TextField,
    Text,
    SnackBar,
    Row,
    BarChart
)

from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment

from app.src.crud.user_crud import get_user_by_email, get_user_by_username
from app.src.components.base import WithDB
from app.src.utils import switch_view
from app.src.views.calculator import calculator


class InputColumn(WithDB, Column):
    ...


class GraphColumn(WithDB, Column):
    ...


class CalculatorComponents(WithDB, Row):
    ...
