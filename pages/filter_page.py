import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Filter_page(Base):

    def __init__(self,  driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    filter_sort = '//h2[@class="facets__heading"]'
    brand = '//details[@id="Details-1-template--20875138728203__main"]'
    brand_nike = '//label[@for="Filter-filter.p.vendor-15"]'
    category = '//details[@id="Details-4-template--20875138728203__main"]'
    category_footwear = '//label[@for="Filter-filter.p.product_type-3"]'
    size = '//details[@id="Details-7-template--20875138728203__main"]'
    size_value = '//label[@for="Filter-filter.v.option.size-2"]'
    apply_filters = '//button[@class="button button-primary"]'

    #Getters

    def get_filter_sort(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_sort)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_brand_nike(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_nike)))

    def get_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category)))

    def get_category_footwear(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_footwear)))

    def get_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size)))

    def get_size_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_value)))

    def get_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filters)))


    #Actions

    def click_filter_sort(self):
        self.get_filter_sort().click()
        print('Click filter&sort')

    def click_brand(self):
        self.get_brand().click()
        print('Click filter brand')

    def click_brand_nike(self):
        self.get_brand_nike().click()
        print('Click brand nike')

    def click_category(self):
        self.get_category().click()
        print('Click filter category')

    def click_category_footwear(self):
        self.get_category_footwear().click()
        print('Click category footwear')

    def click_size(self):
        self.get_size().click()
        print('Click filter size')

    def click_size_value(self):
        self.get_size_value().click()
        print('Click size value')

    def click_apply_filters(self):
        self.get_apply_filters().click()
        print('Click apply filters')


    """Метод, для выставления фильтров"""

    def select_filter(self):
        self.get_current_url()
        time.sleep(2)
        self.click_filter_sort()
        self.click_brand()
        self.click_brand_nike()
        time.sleep(2)
        self.click_category()
        self.click_category_footwear()
        time.sleep(2)
        self.click_size()
        self.click_size_value()
        time.sleep(2)
        self.click_apply_filters()


