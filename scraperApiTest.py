#! /usr/bin/env python3
# scraperApiTest.py - Giving ScraperApi.com a test run.

import requests
import bs4
import pprint

apiKey = 'd7929f4f15170c8d4a08e120c0eec422'

url = 'https://www.tripadvisor.com/Hotels-g293925-Ho_Chi_Minh_City-Hotels.html'

headers = {
    'Accept': 'application/json'
}

res = requests.get('http://api.scraperapi.com/?key=' + apiKey + '&url=' + url, headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

pprint.pprint(soup)

print('Done.')
