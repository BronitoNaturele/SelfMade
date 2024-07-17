from playwright.sync_api import Page
import config
import re
import time


class IndexPage:
    # переменная с путём для картинки
    _Picture_Demo_Web_Shop_ = "//body/div/div/div/div/a/img"
    # переменная с сылкой, на картинке
    _Link_Demo_Web_Shop_ =  '//body/div/div/div/div/a[@href="/"]'
    # метод, который открывает нашу страницу
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    # метод поиска картинки по тексту
    def get_element_and_text_from_attribute_on_main_page(self, page: Page) -> None:
        # локатор, который ищет элемент по атрибуту
        locator_Picture_Demo_Web_Shop_ = page.locator(self._Picture_Demo_Web_Shop_).get_attribute('alt')
        # возвращаяем, найденный выше атрибут в строку
        return locator_Picture_Demo_Web_Shop_


    def clicking_on_the_link(self, page: Page) -> None:
        page.locator(self._Link_Demo_Web_Shop_).click(button="right")
        time.sleep(2)
        page.keyboard.press('ArrowDown')
        time.sleep(2)
        page.keyboard.press('Enter')
