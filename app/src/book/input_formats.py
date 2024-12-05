from flet import Text, TextField, Row, Page


class LeftSided(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x = TextField(label='x', width=60, height=40)
        self.controls = [
            Row(
                controls=[
                    Text(value='P(X<='),
                    self._x,
                    Text(value=')'),
                ],
            ),
        ]

    @property
    def x(self):
        return self._x.value


class RightSided(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x = TextField(label='x')
        self.controls = [
            Row(
                controls=[
                    Text(value='P('),
                    self._x,
                    Text(value='<=X)')
                ]
            ),
        ]

    @property
    def x(self):
        return self._x.value


class Interval(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x1 = TextField(label='x1')
        self._x2 = TextField(label='x2')
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

    @property
    def x1(self):
        return self._x1.value

    @property
    def x2(self):
        return self._x2.value
