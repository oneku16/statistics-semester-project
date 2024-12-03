from flet import Page, Control


def switch_view(page: Page, control: Control) -> None:
    page.clean()
    page.add(control)
    page.update()
