import asyncio
from logging import getLogger

from flet import (
    app,
    Page,
    Text,
)
import flet.version

logger = getLogger(__name__)


async def main(page: Page) -> None:
    await asyncio.sleep(1)
    page.title = "Calculator"
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
        "RobotoSlab": "RobotoSlab[wght].ttf",
    }
    page.add(Text("Test!"))


if __name__ == '__main__':
    app(target=main)
