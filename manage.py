from collectors.base_scraper import BaseScraper


if __name__ == '__main__':
    input_url = input('give me url: ')
    print('Starting...')
    scraper = BaseScraper()
    print('Init complete')
    p_links = scraper.get_product_links_list(
        input_url, scraper.config.getint('main', 'number_of_pages_to_parse'))
    result_list = []
    for i in p_links:
        print(f'working with {i}')
        if scraper.collect_data(i):
            result_list.append(i)

    scraper.close_browser()

    with open('output.txt', 'w') as file:
        file.writelines('\n'.join(result_list))
