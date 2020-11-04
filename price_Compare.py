from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

source1="https://www.reliancedigital.in/apple-iphone-11-pro-max-64-gb-midnight-green-smartphone/p/491584687"
source2="https://www.flipkart.com/apple-iphone-11-pro-max-midnight-green-64-gb/p/itmab1763b5ca244?pid=MOBFKCTSRYPAQNYT&fm=organic&ssid=06ixd4lwz40000001604483934546"
source3="https://www.croma.com/apple-iphone-11-pro-max-midnight-green-64-gb-4-gb-ram-/p/221131"

# creating a webdriver object for Chrome-option and Configure
wait_imp = 10
CO=webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension',False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')

wd =webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe',options=CO)

print("Connecting to Reliance Digital")
wd.get(source1)
wd.implicitly_wait(wait_imp)
relianceDigital_price=wd.find_element_by_xpath("//span[@class='pdp__offerPrice']")
r_price=relianceDigital_price.text

print(" -------> Successfully retrieved the Price of the Product from 'reliancedigital.in'")
time.sleep(4)

print("Connecting to Flipkart")
wd.get(source2)
wd.implicitly_wait(wait_imp)
flipkart_price=wd.find_elements_by_xpath("//div[@class='_1vC4OE _3qQ9m1']")
f_price=flipkart_price[0].text

print(" ------> Successfully retrieved the Price of the Product from 'flipkart.com'")
time.sleep(4)

print("Connecting to Croma")
wd.get(source3)
wd.implicitly_wait(wait_imp)
croma_price=wd.find_elements_by_xpath("//span[@class='amount']")
c_price=croma_price[0].text

print(" ------> Successfully retrieved the Price of the Product from 'croma.in'")

print("Price available at Reliance Digital is "+r_price)
print("Price available at Flipkart is "+f_price)
print("Price available at Croma is "+c_price)

wd.quit()