#! /usr/bin/env python3
# downloadXkcd2.py - Downloads all XKCD comics.

import requests
import os
import bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # TODO: Find the url of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'https:' + comicElem[0].get('src')
    # TODO: Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            continue
    # TODO: Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
print('Done.')
