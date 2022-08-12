#! /usr/bin/env python3
# compFind.py - A handy competitor data-search tool. Takes a command line argument for a city and returns useful data.

import sys
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import OrderedDict

chromedriver = '/Users/dan/WebDriver/chromedriver'
apiKey = 'd7929f4f15170c8d4a08e120c0eec422'
hotelData = OrderedDict()

# Command line arguments
if len(sys.argv) < 2:
    print('Usage: compFind.py city country luxury|budget')
    sys.exit()


def searchForHotels(cityCountryRating):  # Search Google using command arguments, click 'I'm feeling lucky' to get Tripadvisor url
    print('Loading Google.com...')
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode

    # Launch google in the browser
    browser = webdriver.Chrome(chromedriver, options=opts)
    browser.get('https://www.google.com')

    # Click "English" if necessary (VPN usage) - not working atm
    #elemEnglish = browser.find_element_by_xpath('//*[@id="SIvCob"]/a')
    # if elemEnglish.text == "English":
    # elemEnglish.click()

    # Input search query
    elemSearch = browser.find_element_by_xpath('//*[@id="lst-ib"]')
    elemSearch.send_keys('Tripadvisor hotels ' + cityCountryRating)

    # Click I'm feeling lucky
    print('Loading Tripadvisor results...')
    elemLucky = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[2]')
    elemLucky.click()

    # Get url for request
    currentUrl = browser.current_url
    browser.quit()
    return currentUrl


def requestPage(url):  # Request hotel data via API
    print('Fetching hotel data...')
    headers = {'Accept': 'application/json'}
    res = requests.get('http://api.scraperapi.com/?key=' + apiKey + '&url=' + url, headers=headers, timeout=60)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup


def appendDict(dic, list):
    for d, l in zip(dic, list):
        hotelData[d].append(l)


def extractData(soup):  # Save hotel data to a dictionary
    # Create lists to store soup data
    hotelPrices = []
    hotelRatings = []
    hotelSnippets = []
    # Loop through all the listings on each page to group data
    divs = soup.find_all('div', {'class': 'prw_rup prw_meta_hsx_responsive_listing ui_section listItem'})
    for div in divs:
        # Add hotel names as keys in hotelData Dict
        for div in soup.find_all('div', {'class': 'listing_title'}):
            hotelData[div.text.strip()] = []
    # Add hotel prices as values in hotelData Dict
        for div in soup.find_all('div', {'class': 'price autoResize'}):
            hotelPrices.append(div.text.strip())
    appendDict(hotelData, hotelPrices)


url = searchForHotels(' '.join(sys.argv[1:]))
soup = requestPage(url)
hotels = extractData(soup)
print(hotelData)

# for num, name in enumerate(hotelData, 1):
#    print(num, name)

# IDEA: Allow users to specify search country of origin for more accurate results.
