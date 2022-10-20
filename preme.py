
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

    category = ''
    #this is used to edit the url accordingly
    #categories choices are: new, jackets, shirts, tops_sweaters, sweatshirts, pants, shorts, t-shirts, hats, bags accessories, shoes, or skate
    itemcolor = ''
    size = ''

    itemxpath = str("//*[contains(text(),'"+itemcolor+"')]")
    print(itemxpath)

    sizexpath2 = str("//*[@id='size']/option[contains(text(), '"+size+"')]")
    print(sizexpath2)

    opts = Options()
    opts.add_argument('--log-level=0') 
    opts.add_argument("--disable-notifications")
    #If you want to use proxy enter it in place of PROXYHERE; delete #s
    ##PROXY = 'PROXYHERE'
    #opts.add_argument('--proxy-server=%s' % PROXY)
    driver = uc.Chrome(use_subprocess=True, version_main=104, options=opts, service_args=["--log-path=thelog.txt"])
    wait = WebDriverWait(driver,20)



    # LIST ALL CATEGORIES
    driver.get('https://www.supremenewyork.com/shop/all/'+category)
    driver.maximize_window()

    
    
    finditem = driver.find_element(By.XPATH, (itemxpath))
    finditem.click()
    #time.sleep(3)

    
    size = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ('#size'))))
    size.click()
    
    findsize = wait.until(EC.element_to_be_clickable((By.XPATH, (sizexpath2))))
    findsize.click()
    time.sleep(0.05)
    
    size.click()
    time.sleep(0.1)

    addit0 = driver.find_element(By.NAME, "commit")
    addit0.click()

    time.sleep(0.4)

    ##addit1 = driver.find_element(By.XPATH, ("//*[contains(text(),'checkout now')]"))
    #addit1 = wait.until(EC.presence_of_element_located(((By.CLASS_NAME, 'button checkout'))))
    #addit1.click()

    driver.get('https://www.supremenewyork.com/checkout')

    time.sleep(0.5)

    buy0 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ('#order_billing_name'))))
    buy0.send_keys(name)

    buy1 = driver.find_element(By.CSS_SELECTOR, ('#order_email'))
    buy1.send_keys(email)

    buy2 = driver.find_element(By.CSS_SELECTOR, ('#order_tel'))
    buy2.send_keys(tel)

    buy3 = driver.find_element(By.CSS_SELECTOR, ('#order_billing_address'))
    buy3.send_keys(address)

    buy4 = driver.find_element(By.CSS_SELECTOR, ('#order_billing_address_2'))
    if len(address2)>0:
        buy4.send_keys(address2)

    buy5 = driver.find_element(By.CSS_SELECTOR, ('#order_billing_zip'))
    buy5.send_keys(zipcode)

    # = driver.find_element(By.CSS_SELECTOR, ('#order_billing_city'))

    buy6 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_number'))
    buy6.send_keys(number)

    buy7 = driver.find_element(By.CSS_SELECTOR, ('#vvr > div.input.string.required.credit_card_month'))
    buy7.click()
   # driver.execute_script("arguments[0].click();", buy7)

    #buy7.send_keys(month)
    buy8 = wait.until(EC.presence_of_element_located((By.XPATH, ("//*[@id='credit_card_month']/option[contains(text(), "+month+")]"))))
    #buy8 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_month > option:nth-child(1)'))
    buy8.click()

    ###this is a combobox, 4 second line each child corresponds 2 month

    buy9 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_year'))
    buy9.send_keys(year)

    #buy10 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_year > option:nth-child(2)')) 
    ###same deal hear except starts w 2, 2 = 22, runs up to 11 or 2032
    buy11 = driver.find_element(By.CSS_SELECTOR, ('#credit_card_verification_value'))
    buy11.send_keys(ccv)


    time.sleep(0.1)
    check = driver.find_element(By.CSS_SELECTOR, ('#terms-checkbox > label > div > ins'))
    check.click()
    ###^checkbox 4 agreement

    pay = driver.find_element(By.CSS_SELECTOR, ('#pay > input'))
    pay.click() 
    ###process payment button
    
    time.sleep(30)
    
    #cancel = driver.find_element(By.CSS_SELECTOR, ('#pay > a'))
    #cancel.click()
    ###cancel order button

copit()
     
