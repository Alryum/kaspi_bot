from collectors.base_scraper import BaseScraper


if __name__ == '__main__':
    scraper = BaseScraper()
    # scraper.collect_data('https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-128-gb-goluboi-104417308/?c=750000000#!/item')
    p_links = scraper.get_product_links_list(
        'https://kaspi.kz/shop/c/home%20equipment/', 1)
    result_list = []
    for i in p_links:
        if scraper.collect_data(i):
            result_list.append(i)

    print(result_list)
