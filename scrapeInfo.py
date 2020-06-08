import requests
import pandas as pd
from bs4 import BeautifulSoup

def main():
    titles = []
    prices = []
    ratings = []

    for i in range(1,51):
        html_page = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html')
        content = html_page.content
        soup = BeautifulSoup(content, 'html.parser')
        book_sections = soup.find_all('article', class_='product_pod')
        
        for book in book_sections:
            title = book.h3.a.get('title')
            price = book.find('p', class_='price_color').text
            rating = getRating(book.p.get('class')[1])

            # append to array to store all
            titles.append(title)
            prices.append(price)
            ratings.append(rating)

    df = pd.DataFrame({
        'titles': titles,
        'prices': prices,
        'ratings': ratings,
    })
    df.to_csv('bookinfo.csv', index=False)

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

if __name__ == '__main__':
    main()
