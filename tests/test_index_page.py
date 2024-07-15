import pytest
import pages


class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.get_element_and_text_from_attribute_on_main_page(page)
        actual_result = pages.index_page.get_element_and_text_from_attribute_on_main_page(page)
        assert actual_result == "Tricentis Demo Web Shop"