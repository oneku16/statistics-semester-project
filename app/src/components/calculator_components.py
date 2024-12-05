from cProfile import label
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


class CalculatorsDropdown(Dropdown):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.value = CalculatorsEnum.NORMAL.value
        self.options = self.get_options()

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
        self.calculators_dropdown = self.__build_calculators_dropdown()
        self.calculator = self.__build_calculator()
        self.interval = self.__build_interval()
        self.params = self.__build_calculator_params()
        self.controls = [
            self.calculators_dropdown,
            self.interval,
            self.params,
            LeftSided(page=self.page)
        ]
        self.page.update()

    def __build_calculators_dropdown(self) -> Dropdown:
        calculators_dropdown = Dropdown(
                on_change=self.calculators_dropdown_on_change,
                value=CalculatorsEnum.NORMAL.value,
                options=[
                    dropdown.Option(member.value) for member in CalculatorsEnum
                ]
            )
        return calculators_dropdown

    def __build_calculator(self, calculator_key: str = '') -> object:
        calculator_key = calculator_key or self.calculators_dropdown.value
        calculator_class = SELECTOR[calculator_key]
        calculator = calculator_class()
        return calculator

    def __build_calculator_params(self) -> Column:
        column = Column(
            controls=[
                    TextField(label=param) for param in self.__get_calculator_params()
            ]
        )
        return column

    def __get_calculator_params(self):
        params = list()
        for key, _ in self.calculator.__getstate__().items():
            if key.startswith('_param_'):
                key = key.replace('_param_', '')
                params.append(key)
        return params

    def calculators_dropdown_on_change(self, event):
        calculator = self.__build_calculator(self.calculators_dropdown.value)
        self.calculator = calculator
        self.calculator = self.__build_calculator()
        self.params = self.__build_calculator_params()
        self.controls[-2] = self.params
        self.page.update()

    def __build_interval(self) -> Row:
        row = Row(
            controls=[
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
            ],
        )
        return row

    def select_input_format(self, input_format):
        self.controls[-1] = input_format(page=self.page)
        self.page.update()


class GraphColumn(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page


class CalculatorComponent(WithDB, Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        # self.controls = [
        #     # header
        #     Row(
        #         controls=[
        #
        #         ],
        #     ),
        #     # main row
        #     Row(
        #         controls=[
        #             # input column
        #             Column(
        #                 controls=[
        #
        #                 ],
        #             ),
        #             # graph column
        #             Column(
        #                 controls=[
        #
        #                 ],
        #             ),
        #         ],
        #     ),
        # ]


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
