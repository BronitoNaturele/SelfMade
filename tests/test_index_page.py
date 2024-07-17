import pytest
import pages


class TestFooter:

    def test_user_should_be_able_to_open_main_page(self, page):
        # открытие стартовой страницы
        pages.index_page.open_index_page(page)
        # нахождение элемента по тексту в атрибуте, на стартовой странице
        pages.index_page.get_element_and_text_from_attribute_on_main_page(page)
        # переменная с текстом из атрибута
        actual_result = pages.index_page.get_element_and_text_from_attribute_on_main_page(page)
        # проверка соответствия текстов
        assert actual_result == "Tricentis Demo Web Shop"
        print('Have a text')


    def test_user_when_you_click_on_the_image_the_link_opens(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.clicking_on_the_link(page)

