from playwright.sync_api import Page
from playwright.sync_api import expect
import config
import re


class IndexPage:
    # метод, который открывает нашу страницу
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    # метод поиска картинки по тексту
    def get_text_from_alt_text_on_main_page (self, page: Page) -> None:
        locator = page.get_by_alt_text("Tricentis Demo Web Sho")
        return locator
        expect(locator).to_contain_text("Tricentis Demo Web Shop")
