from playwright.sync_api import Page
import config
import re


class IndexPage:
    # переменная с путём для картинки
    _Picture_Demo_Web_Shop_ = "//body/div/div/div/div/a/img"
    # метод, который открывает нашу страницу
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    # метод поиска картинки по тексту
    def get_element_and_text_from_attribute_on_main_page(self, page: Page) -> None:
        # локатор, который ищет элемент по альтернативному тексту
        return page.locator(self._Picture_Demo_Web_Shop_).get_attribute("alt")

