from collectors.base_scraper import BaseScraper


if __name__ == '__main__':
    scraper = BaseScraper()
    scraper.collect_data('https://kaspi.kz/shop/c/smartphones/?sort=rating')