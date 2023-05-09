from app import Scraper


def main(keyword, count):
    scraper = Scraper(keyword, count)
    scraper.check_enough_or_not()
    scraper.load_more_product()
    scraper.write_to_excel()


if __name__ == '__main__':
    main("kot pantolon", 150)

