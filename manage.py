from collectors.base_scraper import BaseScraper


if __name__ == '__main__':
    print('Starting...')
    scraper = BaseScraper()
    print('Init complete')
    p_links = scraper.get_product_links_list(
        'https://kaspi.kz/shop/c/wireless%20chargers/?q=%3AavailableInZones%3AMagnum_ZONE1%3Acategory%3AWireless%20chargers&sort=rating&sc&page=1', 4)
    result_list = []
    for i in p_links:
        print(f'working with {i}')
        if scraper.collect_data(i):
            result_list.append(i)

    scraper.close_browser()

    with open('output.txt', 'w') as file:
        file.writelines('\n'.join(result_list))
