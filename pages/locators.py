from selenium.webdriver.common.by import By


class YandexMainPagesLocators:

    INPUT_FIELD = (By.XPATH, "//input[@id='text']")
    POPUP = (By.CLASS_NAME, 'mini-suggest__overlay_visible')
    IMAGES_LINK = (By.XPATH, "//a[@data-id='images']")


class YandexImagesPageLocators:

    FIRST_CATEGORY = (By.XPATH,
     "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']//div[@class='PopularRequestList-SearchText']")
    CATEGORY_INPUT_FIELD = (By.XPATH, "//input[@name='text']")
    FIRST_IMAGE = (By.XPATH, "//*[@role='listitem']/div/a")
    IMAGE_FULLSCREEN = (By.XPATH, "//img[@class='MMImage-Origin']")
    NEXT_IMAGE_BTN = (By.CLASS_NAME, "CircleButton_type_next")
    PREV_IMAGE_BTN = (By.CLASS_NAME, "CircleButton_type_prev")
    FOR_SOURCE_OF_IMAGE = (By.XPATH, '//img[@class="MMImage-Origin"]')


class YandexResultsPageLocators:

    RESULTS = (By.XPATH, '//*[@id="search-result"]/li/div/div/div/a')






