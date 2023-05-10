from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


class BaseScraper:
    def __init__(self):
        self.service = FirefoxService(
            executable_path='Z:\alryum\python_projects\kaspi_bot\drivers\geckodriver.exe')
        self.driver = None

    def __start_browser(self):
        '''
        Инициализирует драйвер
        '''
        self.driver = Firefox(service=self.service)

    def __navigate_to_website(self, url):
        '''
        Переход на страницу
        '''
        self.driver.get(url=url)

    def __solve_location_dialog(self):
        '''
        Во всплывающем окне выбирает город Алматы
        '''
        city_li = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div[1]/div/ul[1]/li[9]/a')
        city_li.click()

    def collect_data(self, url_source: str):
        if not self.driver:
            self.__start_browser()
        self.__navigate_to_website(url=url_source)
        
        self.__solve_location_dialog()


    def close_browser(self):
        '''
        Закрывает активную сессию
        '''
        if self.driver:
            self.driver.quit()
