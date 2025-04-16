import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Product_page(Base):

    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    select_product_1 = '(//a[@class="absolute block h-full left-0 top-0 w-full"])[1]'
    name_product = '//h2[@class="h1 mt-1.5 mb-0 text-xl font-normal text-black break-words"]'
    price_product = '//*[@id="price-product-page-form"]/div/div/div[2]/span[2]'
    size_product = '//label[@data-size="36"]'
    add_to_cart = '//button[@id="ProductSubmitButton-product-page-form"]'
    view_cart = '//a[@class="button button-inverse-pill !py-5 !mt-2.5 text-xs"]'


    #Getters

    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_size_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_product)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_view_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.view_cart)))


    #Actions

    def click_select_product(self):
        self.get_select_product().click()
        print('Click select product')

    def click_size_product(self):
        self.get_size_product().click()
        print('Click size product')

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print('Click add to cart')

    def click_view_cart(self):
        self.get_view_cart().click()
        print('Click view cart')

    #Method

    def select_product(self):
        self.get_current_url()
        self.click_select_product()
        print(f'Name product: {self.get_name_product().text}')
        print(f'Price product: {self.get_price_product().text}')
        self.click_size_product()
        self.click_add_to_cart()
        time.sleep(2)
        self.click_view_cart()
