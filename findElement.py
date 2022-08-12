from selenium import webdriver
chromedriver = '/Users/dan/WebDriver/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('card-block')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
