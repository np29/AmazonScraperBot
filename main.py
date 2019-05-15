import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import html
import time

url = "https://www.amazon.com/gp/sign-in.html"
browser = webdriver.Chrome()
browser.get(url)

#content = browser.page_source
#html_doc = html.fromstring(content)

email_box = browser.find_element_by_id("ap_email")
password_box = browser.find_element_by_id("ap_password")
email_box.send_keys("braveharambe@gmail.com")
password_box.send_keys("1234Neel$")
browser.find_element_by_id("signInSubmit").click()

request_browser_cookies = browser.get_cookies()

giveawaysUrl = "https://www.amazon.com/ga/giveaways?ref_=aga_dp_lm"
browser.get(giveawaysUrl)


giveAways = browser.find_element_by_xpath("//div[@id='reactApp']")
print(giveAways)
time.sleep(2)
print("*************************************")
items = giveAways.find_elements_by_tag_name("li")
print(items)

# for item in items:
#     item.click()
#     browser.back()
