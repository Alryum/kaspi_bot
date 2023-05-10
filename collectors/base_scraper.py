from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


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

        # /html/body/div[1]/div[5]/div/div[2]/div/ul/li[2]

    def __load_all_reviews(self):
        '''
        После загрузки страницы товара переходит на вкладку отзывов и загружает все отзывы
        '''
        reviews_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/ul/li[2]')
        reviews_button.click()
        while True:
            try:
                button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.reviews__view-change:nth-child(1)')))

                # more_button = self.driver.find_element(By.CSS_SELECTOR, 'a.reviews__view-change:nth-child(1)')

                # more_button.click()
                # time.sleep(1)

                button.click()
            except:
                # если кнопка не найдена, то выходим из цикла
                break

    def collect_data(self, url_source: str):
        if not self.driver:
            self.__start_browser()
        self.__navigate_to_website(url=url_source)
        
        self.__solve_location_dialog()
        self.__load_all_reviews()


    def close_browser(self):
        '''
        Закрывает активную сессию
        '''
        if self.driver:
            self.driver.quit()
