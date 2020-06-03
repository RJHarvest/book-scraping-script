import os
import csv
import requests
import urllib.request
from bs4 import BeautifulSoup

domain = 'http://books.toscrape.com'

def scrape():
    thumbnail_urls = []

    for i in range(1,50):
        html_page = requests.get(f'{domain}/catalogue/page-{i}.html')
        content = html_page.content
        soup = BeautifulSoup(content, 'html.parser')
        thumbnails = soup.find_all('img', class_='thumbnail')

        for thumbnail in thumbnails:
            thumbnail_info = []

            # get data
            thumbnail_src = thumbnail.get('src')
            name = thumbnail.get('alt')
            thumbnail_url = formatThumbnailUrl(thumbnail_src)
            
            # store data in array
            thumbnail_info.append(thumbnail_url)
            thumbnail_info.append(name)

            # store array in array
            thumbnail_urls.append(thumbnail_info)

    return thumbnail_urls

def formatThumbnailUrl(thumbnail_src):
    thumbnail_src = thumbnail_src.replace('..', '')
    url = domain + thumbnail_src
    return url

def storeImagesToFolder(thumbnails):
    imageUrlsLength = len(thumbnails)
    folderExists = os.path.exists('./images')

    if (imageUrlsLength == 0):
        return

    if (not folderExists):
        os.system('mkdir images')
    
    for thumbnail in thumbnails:
        name = thumbnail[1].replace(' ', '_')
        url = thumbnail[0]
        print(name)
        urllib.request.urlretrieve(url, f'./images/{name}.jpg')

def main():
    # step 1: scrape all
    thumbnails = scrape()
    # step 2: store data in csv file
    storeImagesToFolder(thumbnails)

if __name__ == '__main__':
    main()
