from flet import Text, TextField, Row, Page


class LeftSided(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x = TextField(label='x')
        self.controls = [
            Text(value='P(X<= '),
            self._x,
            Text(value=')')
        ]
        self.page.update()

    @property
    def x(self):
        return self._x.value


class RightSided(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self._x = TextField(label='x')
        self.controls = [
            Text(value='P('),
            self._x,
            Text(value='<=X)')
        ]
        self.page.update()

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
            Text(value='P('),
            self._x1,
            Text(value='X<=X'),
            self._x2,
        ]

    @property
    def x1(self):
        return self._x1.value

    @property
    def x2(self):
        return self._x2.value
