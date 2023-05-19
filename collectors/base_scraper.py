from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from collections import Counter
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
        try:
            city_li = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div[1]/div/ul[1]/li[9]/a')
            city_li.click()
        except:
            pass


    def __load_all_reviews(self):
        '''
        После загрузки страницы товара переходит на вкладку отзывов и загружает все отзывы
        '''
        reviews_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/ul/li[2]')
        reviews_button.click()
        while True:
            try:
                button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.reviews__view-change:nth-child(1)')))
                button.click()
            except:
                break

    
    def __get_amount_of_new_reviews(self):
        reviews = self.driver.find_elements(By.CLASS_NAME, 'reviews__date')
        reviews_date_list = []
        for i in reviews:
            reviews_date_list.append(i.text[3:])
        date_counts = Counter(reviews_date_list)
        reviews_counter = 0
        for date, count in date_counts.items():
            if '2023' in str(date):
                reviews_counter += int(count)
        
        return reviews_counter



    def get_product_links_list(self, url, amount_of_pages):
        '''
        собирает ссылки на все товары в категории, до необходимой страницы
        '''
        if not self.driver:
            self.__start_browser()
        self.__navigate_to_website(url)
        self.__solve_location_dialog()
        links_list = []

        for i in range(amount_of_pages):
            product_list = self.driver.find_elements(By.CLASS_NAME, 'item-card__image-wrapper')
            links_list.extend([i.get_attribute('href') for i in product_list])
            try:
                next_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#scroll-to > div.item-cards-grid > div.pagination > li:nth-child(7)')))
                next_btn.click()
            except:
                break  
        
        return links_list


    def collect_data(self, url_source):
        if not self.driver:
            self.__start_browser()
        self.__navigate_to_website(url=url_source)
        
        self.__solve_location_dialog()
        self.__load_all_reviews()
        if self.__get_amount_of_new_reviews() >= 10:
            return True
        return False


    def close_browser(self):
        '''
        Закрывает активную сессию
        '''
        if self.driver:
            self.driver.quit()
