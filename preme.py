
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def copit():
    name = ''
    email = ''
    tel = ''
    address = ''
    address2 = ''
    #enter unit # for apts here
    zipcode = ''
    number = ''
    month = ''
    year = ''
    ccv = ''

    opts = Options()
    opts.add_argument('--log-level=0') 
    opts.add_argument("--disable-notifications")
    #If you want to use proxy enter it in place of PROXYHERE; delete #s
    ##PROXY = 'PROXYHERE'
    #opts.add_argument('--proxy-server=%s' % PROXY)
    driver = uc.Chrome(use_subprocess=True, version_main=104, options=opts, service_args=["--log-path=thelog.txt"])
    
    driver.get('https://wtfismyip.com/')
    driver.maximize_window()

    size = driver.find_element(By.CSS_SELECTOR, ('#size'))  
    size.click()
    sizelist = driver.find_element(By.CSS_SELECTOR, ('#size > option:nth-child(1)')) 
    sizelist.click()

    addit0 = driver.find_element(By.CSS_SELECTOR, ('add-remove-buttons > input'))
    addit0.click()

    addit1 = driver.find_element(By.CSS_SELECTOR, ('cart > a.button.checkout'))
    addit1.click()

    buy0 = driver.find_element(By.CSS_SELECTOR, ('#order_billing_name'))
    buy0.sendkeys(name)

    buy1 = driver.find_element(By.CSS_SELECTOR, ('#order_email'))
    buy1.sendkeys(email)

    buy2 = driver.find_element(By.CSS_SELECTOR, ('#order_tel'))
    buy2.send_keys(tel)

    buy3 = driver.find_element(By.CSS_SELECTOR, ('#order_billing_address'))
    buy3.send_keys(address)

    buy4 = driver.find_element(By.CSS_SELECTOR, ('#order_billing_address_2'))
    if len(address2)>0:
        buy4.sendkeys(address2)

    buy5 = driver.find_element(By.CSS_SELECTOR, ('#order_billing_zip'))
    buy5.send_keys(zipcode)

    # = driver.find_element(By.CSS_SELECTOR, ('#order_billing_city'))

    buy6 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_number'))
    buy6.send_keys(number)

    buy7 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_month'))
    
    buy7.send(month)

    #buy8 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_month > option:nth-child(1)'))
    ###this is a combobox, 4 second line each child corresponds 2 month

    buy9 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_year'))
    buy9.send_keys(year)

    #buy10 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_year > option:nth-child(2)')) 
    ###same deal hear except starts w 2, 2 = 22, runs up to 11 or 2032
    buy11 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_verification_value'))
    buy11.send_keys(ccv)

    check = driver.find_element(By.CSS_SELECTOR, ('#terms-checkbox > label > div > ins'))
    check.click()
    ###^checkbox 4 agreement

    pay = driver.find_element(By.CSS_SELECTOR, ('#pay > input'))
    pay.click() 
    ###process payment button
    cancel = driver.find_element(By.CSS_SELECTOR, ('#pay > a'))
    cancel.click()
    ###cancel order button
   
     
