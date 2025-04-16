import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.filter_page import Filter_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.product_page import Product_page


def test_select_product():
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    time.sleep(3)

    print('Start Test')

    """Выбор категории на главной странице"""
    mp = Main_page(driver)
    mp.select_category()

    """Выставление фильтров"""
    fp = Filter_page(driver)
    fp.select_filter()

    """Выбор товара"""
    pp = Product_page(driver)
    pp.select_product()

    """"Проверка товара в корзине"""
    cp = Cart_page(driver)
    cp.cart_product()

    """Заполнение информации о клиенте"""
    cip = Client_information_page(driver)
    cip.input_information()

    """Проверка url. Делаем скриншот"""
    fp = Finish_page(driver)
    fp.finish()

    time.sleep(3)
    driver.quit()
