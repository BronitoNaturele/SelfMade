from playwright.sync_api import Page
from playwright.sync_api import expect
import config
import re


class IndexPage:
    # переменная с локатором, который ищет элемент по альтернативному тексту
    _Picture_Demo_Web_Shop_ = page.get_by_alt_text("Tricentis Demo Web Shop")
    # метод, который открывает нашу страницу
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    # метод поиска картинки по тексту
    def get_text_from_alt_text_on_main_page(self, page: Page) -> None:
        return page.locator(self._Picture_Demo_Web_Shop_).get_attribute('src')
        expect(locator).to_contain_text("Tricentis Demo Web Shop")
