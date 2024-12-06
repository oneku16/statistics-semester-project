from flet import Text, TextField, Row, Page


class LeftSided(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x = TextField(
            label='x',
            width=80,
            height=40,
            text_size=14,
        )
        self.controls = [
            Row(
                controls=[
                    Text(value='P(X<='),
                    self._x,
                    Text(value=')'),
                ],
            ),
        ]
        self.page.update()

    @property
    def x(self):
        return self._x.value

    def get_params(self):
        if self._x.value == '':
            return tuple()
        return float(self._x.value),

    def __str__(self):
        return 'LeftSided'

    def __repr__(self):
        return 'LeftSided'


class RightSided(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x = TextField(
            label='x',
            width=80,
            height=40,
            text_size=14,
        )
        self.controls = [
            Row(
                controls=[
                    Text(value='P('),
                    self._x,
                    Text(value='<=X)')
                ]
            ),
        ]
        self.page.update()

    def get_params(self):
        return float(self._x.value),

    def __repr__(self):
        return 'RightSided'

    def __str__(self):
        return 'RightSided'

    @property
    def x(self):
        return self._x.value


class Interval(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x1 = TextField(
            label='x1',
            width=80,
            height=40,
            text_size=14,
        )
        self._x2 = TextField(
            label='x2',
            width=80,
            height=40,
            text_size=14,
        )
        self.controls = [
            Row(
                controls=[
                    Text(value='P('),
                    self._x1,
                    Text(value='X<=X'),
                    self._x2,
                ]
            ),
        ]
        self.page.update()

    @property
    def x1(self):
        return self._x1.value

    @property
    def x2(self):
        return self._x2.value

    def get_params(self):
        return float(self._x1.value), float(self._x2.value),

    def __repr__(self):
        return 'Interval'

    def __str__(self):
        return 'Interval'
