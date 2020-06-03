import os
import csv
import requests
from bs4 import BeautifulSoup

def scrape():
    all_book_infos = []

    for i in range(1,50):
        html_page = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html')
        content = html_page.content
        soup = BeautifulSoup(content, 'html.parser')
        book_sections = soup.find_all('article', class_='product_pod')

        for book in book_sections:
            title = book.h3.a.get('title')
            price = book.find('p', class_='price_color').text
            rating = getRating(book.p.get('class')[1])

            book_info = []
            # append to array to store all
            book_info.append(title)
            book_info.append(rating)
            book_info.append(price)
            all_book_infos.append(book_info)

    return all_book_infos

def getRating(strRating):
    if (strRating == 'One'):
        return 1
    elif (strRating == 'Two'):
        return 2
    elif (strRating == 'Three'):
        return 3
    elif (strRating == 'Four'):
        return 4
    elif (strRating == 'Five'):
        return 5
    else:
        return None

def writeDataToCsv(bookdata):
    header = ['Title', 'Rating', 'Price']
    with open('bookinfo.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(bookdata)

def main():
    # step 1: scrape all
    bookdata = scrape()
    # step 2: store data in csv file
    writeDataToCsv(bookdata)

if __name__ == '__main__':
    main()
