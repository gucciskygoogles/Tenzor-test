import time

import allure
import pytest

from pages.yandex_main import YandexMainPage


class TestScenario:

    """
    Первый тест помечен как ожидаемый к падению, т.к. вероятность наличия ссылок на tenzor.ru
    во всех пяти результатах мала
    """

    @allure.story()
    @pytest.mark.xfail()
    def test_case_one(self, browser, url):
        page = YandexMainPage(browser, url)
        page.open()
        page.should_be_yandex_url()
        search_results = page.search_in_input_field()
        search_results.count_of_results()

    @allure.story()
    def test_case_two(self, browser, url):
        page = YandexMainPage(browser, url)
        page.open()
        image_page = page.going_to_images_page()
        window = browser.window_handles[1]
        browser.switch_to.window(window)
        image_page.should_be_images_page()
        image_page.going_to_first_category()
        assert image_page.get_text_from_input_field() == image_page.get_name_of_category()
        time.sleep(3)
        image_page.open_first_image()
        image_page.check_image_is_fully_open()
        time.sleep(2)
        source_before_click = image_page.get_image_source()
        image_page.next_image_btn_click()
        image_page.prev_image_btn_click()
        time.sleep(2)
        source_after_click = image_page.get_image_source()
        assert source_after_click == source_before_click