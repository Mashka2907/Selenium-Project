import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод, который будет возвращать URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    """Метод, для проверки заголовка"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    """Метод для скриншота"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('E:\\users\\parfenova_me\\PycharmProjects\\SeleniumFinal2\\screen\\' + name_screenshot)

    """Проверка URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')
