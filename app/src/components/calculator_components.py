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
    Container,
)
from flet.core.matplotlib_chart import MatplotlibChart

from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment, TextAlign

from app.src.book.hypergeometric import HyperGeometric
from app.src.book.binomial import Binomial
from app.src.book.normal import Normal
from app.src.components.base import WithDB
from app.src.utils import switch_view
from app.src.book.input_formats import LeftSided, RightSided, Interval
from app.src.views.calculator import calculator


class CalculatorsEnum(Enum):
    NORMAL = "Normal"
    HYPER_GEOMETRIC = "HyperGeometric"
    BINOMIAL = "Binomial"


SELECTOR = {
    'Normal': Normal,
    'HyperGeometric': HyperGeometric,
    'Binomial': Binomial,
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
        self.input_format = self.__default_input_format()
        self.on_solve = self.__build_solve_button()
        self.controls = [
            self.calculators_dropdown,
            self.interval,
            self.params,
            self.input_format,
            self.on_solve,
        ]
        self.page.update()

    def __build_solve_button(self):
        button = ElevatedButton(
            text="Solve",
            on_click=self.__on_solve,
        )
        return button

    def __on_solve(self, event):
        self.page.update()
        for attr, value in self.__get_calculator_values():
            self.calculator.__setattr__(f'_param_{attr}', float(value))

        area, graph = self.calculator.solve(*self.__get_intervals())
        return area, graph

    def __get_intervals(self):
        params = self.input_format.get_params()
        return params

    def __get_calculator_values(self):
        for textfield in self.params.controls:
            if textfield.value is None or textfield.value == '':
                continue
            yield textfield.label, textfield.value

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
        for key in self.calculator.__dict__:
            if key.startswith('_param_'):
                key = key.replace('_param_', '')
                yield key

    def calculators_dropdown_on_change(self, event):
        self.calculator = self.__build_calculator(self.calculators_dropdown.value)
        self.calculator = self.__build_calculator()
        self.params = self.__build_calculator_params()
        self.controls[2] = self.params
        self.page.update()

    def __build_interval(self) -> Row:
        row = Row(
            controls=[
                ElevatedButton(
                    text="Left sided",
                    on_click=lambda _: self.__update_input_format(LeftSided)
                ),
                ElevatedButton(
                    text="Interval",
                    on_click=lambda _: self.__update_input_format(Interval),
                ),
                ElevatedButton(
                    text="Right sided",
                    on_click=lambda _: self.__update_input_format(RightSided)
                )
            ],
        )
        return row

    def __update_input_format(self, input_format):
        self.input_format = input_format(page=self.page)
        self.controls[-2] = self.input_format
        self.page.update()

    def __default_input_format(self):
        return LeftSided(page=self.page)


class GraphColumn(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def set_graph(self, graph):
        fig = MatplotlibChart(
            figure=graph,
            expand=True
        )
        self.controls = [fig]
        print(type(graph))
        print(self.controls)
        self.page.update()


class CalculatorComponent(WithDB, Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.calculator = None
        self.calculators_dropdown = self.__build_calculators_dropdown()
        self.calculator = self.__build_calculator()
        self.interval = self.__build_interval()
        self.params = self.__build_calculator_params()
        self.input_format = self.__default_input_format()
        self.on_solve = self.__build_solve_button()
        self.controls = [
            # header row index=0
            Row(
                controls=[

                ]
            ),
            # main row index=1
            Row(
                controls=[
                    # input column index=0
                    Column(
                        controls=[
                            self.calculators_dropdown,
                            self.interval,
                            self.params,
                            self.input_format,
                            self.on_solve,
                        ]
                    ),
                    # graph column index 1
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                ]
            ),
        ]
        self.page.update()

    def handler_logout(self, event):
        from app.src.components.login_components import LoginReturn as LocalLoginReturn
        self.page.client_storage.remove("user_id")
        self.page.client_storage.remove("username")
        switch_view(page=self.page, control=LocalLoginReturn(page=self.page))
        self.page.update()

    def __build_solve_button(self):
        button = ElevatedButton(
            text="Solve",
            on_click=self.__on_solve,
        )
        return button

    def __on_solve(self, event):
        for attr, value in self.__get_calculator_values():
            self.calculator.__setattr__(f'_param_{attr}', float(value))

        area, graph = self.calculator.solve(*self.__get_intervals())
        if self.controls[1].controls[1].controls:
            self.controls[1].controls[1].controls.clear()
        self.controls[1].controls[1].controls.append(MatplotlibChart(figure=graph, original_size=True, expand=True))
        self.page.update()
        print(area)
        return area, graph

    def __get_intervals(self):
        params = self.input_format.get_params()
        return params

    def __get_calculator_values(self):
        for textfield in self.params.controls:
            if textfield.value is None or textfield.value == '':
                continue
            yield textfield.label, textfield.value

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
        for key in self.calculator.__dict__:
            if key.startswith('_param_'):
                key = key.replace('_param_', '')
                yield key

    def calculators_dropdown_on_change(self, event):
        self.calculator = self.__build_calculator(self.calculators_dropdown.value)
        self.calculator = self.__build_calculator()
        self.params = self.__build_calculator_params()
        self.controls[1].controls[0].controls[2] = self.params
        self.page.update()

    def __build_interval(self) -> Row:
        row = Row(
            controls=[
                ElevatedButton(
                    text="Left sided",
                    on_click=lambda _: self.__update_input_format(LeftSided)
                ),
                ElevatedButton(
                    text="Interval",
                    on_click=lambda _: self.__update_input_format(Interval),
                ),
                ElevatedButton(
                    text="Right sided",
                    on_click=lambda _: self.__update_input_format(RightSided)
                )
            ],
        )
        return row

    def __update_input_format(self, input_format):
        self.input_format = input_format(page=self.page)
        self.controls[1].controls[0].controls[-2] = self.input_format
        self.page.update()

    def __default_input_format(self):
        return LeftSided(page=self.page)

