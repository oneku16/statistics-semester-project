from enum import Enum

from flet import (
    Page,
    Column,
    ElevatedButton,
    TextField,
    Text,
    SnackBar,
    Row,
    BarChart,
    Control,
    Dropdown,
    dropdown,
)

from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment, TextAlign

from app.src.book.hypergeometric import HyperGeometric
from app.src.book.normal import Normal
from app.src.components.base import WithDB
from app.src.utils import switch_view
from app.src.book.input_formats import LeftSided, RightSided, Interval


class CalculatorsEnum(Enum):
    NORMAL = "Normal"
    HYPER_GEOMETRIC = "HyperGeometric"


SELECTOR = {
    'Normal': Normal,
    'HyperGeometric': HyperGeometric,
}


class Intervals(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._interval = None
        self.controls = [
            ElevatedButton(
                text="Left sided",
                on_click=lambda _: self.select_input_format(LeftSided)
            ),
            ElevatedButton(
                text="Interval",
                on_click=lambda _: self.select_input_format(Interval),
            ),
            ElevatedButton(
                text="Right sided",
                on_click=lambda _: self.select_input_format(RightSided)
            )
        ]

    def select_input_format(self, input_format):
        self._interval = input_format(page=self.page)

    @property
    def interval(self):
        if self._interval is None:
            self._interval = LeftSided(page=self.page)
        return self._interval


class CalculatorsDropdown(Dropdown):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.value = CalculatorsEnum.NORMAL.value
        self.options = self.get_options()

    @property
    def real_value(self):
        return self.value

    @property
    def calculator(self):
        return SELECTOR[self.value]

    @staticmethod
    def get_options() -> list[dropdown.Option]:
        result = list()
        for member in CalculatorsEnum:
            result.append(dropdown.Option(member.value))
        return result


class InputColumn(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.calculator = Normal()
        self.interval = LeftSided(page=page)
        self.intervals = Intervals(page=page)
        self.calculators_dropdown = CalculatorsDropdown(page=page)
        self.params = None
        self.controls = [
            self.calculators_dropdown,
            self.intervals,
            *self.real_params,
            *self.interval.controls
        ]

    @property
    def real_params(self):
        if self.params is None:
            self.params = list()
            for param in self.get_params():
                param = param[1:]
                self.params.append(TextField(label=param))
        return self.params

    def get_params(self):
        params = list()
        for key, _ in self.calculator.__getstate__().items():
            if key.startswith('_'):
                params.append(key)
        return params


class GraphColumn(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page


class CalculatorComponent(WithDB, Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.controls = [
            Column(
                controls=[
                    Row(
                        controls=[
                            Text(
                                value="Calculator",
                                weight=FontWeight.BOLD,
                                text_align=TextAlign.CENTER,
                                on_tap=switch_view(self.page, self),
                            ),
                            Text(
                                value="Calculator",
                                weight=FontWeight.BOLD,
                                text_align=TextAlign.RIGHT,
                            ),
                            ElevatedButton(
                                text="Logout",
                                on_click=self.handler_logout,
                                animate_scale=True,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            InputColumn(page=self.page),
                            GraphColumn(page=self.page),
                        ],
                    )
                ]
            ),
        ]

    def handler_logout(self, event):
        from app.src.components.login_components import LoginReturn as LocalLoginReturn
        self.page.client_storage.remove("user_id")
        self.page.client_storage.remove("username")
        switch_view(page=self.page, control=LocalLoginReturn(page=self.page))
        self.page.update()
