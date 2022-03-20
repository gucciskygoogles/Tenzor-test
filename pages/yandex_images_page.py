import allure
from selenium.webdriver import ActionChains
from pages.basepage import BasePage
from pages.locators import YandexImagesPageLocators


class YandexImagesPage(BasePage):

    @allure.step('Проверка наличия страницы')
    def should_be_images_page(self):
        self.should_be_images_url()

    @allure.step
    def should_be_images_url(self):
        assert "https://yandex.ru/images/" in self.browser.current_url

    @allure.step('Клик на первую категорию')
    def going_to_first_category(self):
        first_cat = self.browser.find_element(*YandexImagesPageLocators.FIRST_CATEGORY)
        ActionChains(self.browser).double_click(first_cat).perform()

    @allure.step('Взятие названия категории')
    def get_name_of_category(self):
        first_cat = self.browser.find_element(*YandexImagesPageLocators.FIRST_CATEGORY)
        name_of_category = first_cat.text
        return name_of_category

    @allure.step('Взятие названия категория из поисковой строки')
    def get_text_from_input_field(self):
        inp = self.browser.find_element(*YandexImagesPageLocators.CATEGORY_INPUT_FIELD)
        text = inp.get_attribute("value")
        return text

    @allure.step('Открытие первой картинки')
    def open_first_image(self):
        self.is_element_clickable(*YandexImagesPageLocators.FIRST_IMAGE)

    @allure.step('Проверка того, что картинка полностью открыта')
    def check_image_is_fully_open(self):
        assert self.is_element_present(*YandexImagesPageLocators.IMAGE_FULLSCREEN)

    @allure.step('Взятие ссылки на картинку')
    def get_image_source(self):
        img = self.browser.find_element(*YandexImagesPageLocators.FOR_SOURCE_OF_IMAGE)
        source = img.get_attribute('src')
        return source

    @allure.step('Нажатие на кнопку следующей картинки')
    def next_image_btn_click(self):
        self.is_element_clickable(*YandexImagesPageLocators.NEXT_IMAGE_BTN)

    @allure.step('Нажатие на кнопку предыдущей картинки')
    def prev_image_btn_click(self):
        self.is_element_clickable(*YandexImagesPageLocators.PREV_IMAGE_BTN)