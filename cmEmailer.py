#! /usr/bin/env python3
# cmEmailer.py - Logs into email account and sends an email of the string to the provided address

import sys
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) < 2:
    print('Usage: cmEmailer.py email subject message')
    sys.exit()

chromedriver = '/Users/dan/WebDriver/chromedriver'

# Open browser and navigate to email account login
browser = webdriver.Chrome(chromedriver)
browser.get('https://mail.yahoo.com')
print(browser.current_url)
elemUsername = browser.find_element_by_name('username')

# Input username
print('Enter username:')
elemUsername.send_keys(input())
loginBtn = browser.find_element_by_id('login-signin')
loginBtn.click()

# Input password
wait = WebDriverWait(browser, 10)
elemPassword = wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
loginPassword = getpass.getpass(prompt="Enter password:")
elemPassword.send_keys(loginPassword)
print('Logging in...')
submitBtn = browser.find_element_by_id('login-signin')
submitBtn.click()

# Open a new email
elemCompose = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'btn btn-compose')]")))
elemCompose.click()

# Input sent-to email address
elemTo = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="to-field"]')))
print('Writing email...')
elemTo.send_keys(sys.argv[1])

# Input Subject
elemSubject = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="subject-field"]')))
elemSubject.send_keys(sys.argv[2])

# Input email message
elemMessage = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rtetext"]')))
elemMessage.send_keys(' '.join(sys.argv[3:]))

# Send email
elemSend = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'btn default')]")))
elemSend.click()

print('Email sent to ' + sys.argv[1] + '.')
