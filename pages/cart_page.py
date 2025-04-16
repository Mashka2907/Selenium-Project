from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    cart_word = '(//span[text()="Your Cart"])[1]'
    checkout = '//button[@class="button button-pill w-full bg-primary h-[55px] text-sm mb-0.5 text-white"]'


    #Getters

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))


    #Actions

    def click_checkout(self):
        self.get_checkout().click()
        print('Click checkout')


    #Method

    def cart_product(self):
        self.get_current_url()
        self.assert_word(self.get_cart_word(), 'Your Cart')
        self.assert_url('https://hudsonstore.com/cart')
        self.click_checkout()
