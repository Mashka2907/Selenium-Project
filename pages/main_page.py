from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://hudsonstore.com/'

    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    women = '//details[@id="Details-HeaderMenu-2"]'
    main_word = '//h1[@class="collection-header__title"]'

    # Getters

    def get_women(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.women)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_women(self):
        self.get_women().click()
        print('Click category women')

    #Method

    def select_category(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_women()
        self.assert_word(self.get_main_word(), 'All Womenswear')
