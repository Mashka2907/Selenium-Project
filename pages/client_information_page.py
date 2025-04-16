from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from base.base_class import Base
from faker import Faker


class Client_information_page(Base):
    
    fake = Faker("en_US")

    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    email = '//input[@id="email"]'
    first_name = '(//input[@name="firstName"])[1]'
    last_name = '(//input[@name="lastName"])[1]'
    address = '(//input[@name="address1"])[1]'
    city = '(//input[@name="city"])[1]'
    postal_code = '(//input[@name="postalCode"])[1]'
    phone = '(//input[@name="phone"])[1]'
    total_price = '(//strong[text()="€87.00"])[2]'
    final_name_product = '//p[text()="React Infinity Run Flyknit 3"]'



    #Getters

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_final_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_name_product)))


    #Actions

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input email')

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_address(self, address):
        self.get_address().send_keys(address)
        print('Input address')

    def input_city(self, city):
        self.get_city().send_keys(city)
        print('Input city')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('Input postal code')

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print('Input phone')



    #Method

    def input_information(self):
        fake = Faker("en_US")
        self.get_current_url()
        print(f'Final name product: {self.get_final_name_product().text}')
        print(f'Total price: {self.get_total_price().text}')
        self.input_email(fake.email())
        self.input_first_name(fake.first_name())
        self.input_last_name(fake.last_name())
        self.input_address('32 South St')
        self.input_city('Valletta')
        self.input_postal_code('ABC 1234')
        self.input_phone('+79109109109')

