import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://www.amazon.com/gp/sign-in.html"
session = requests.Session()

driver = webdriver.Firefox()
driver.get(url)
request_browser_cookies = driver.get_cookies()

response = session.get(url)
response_html = response.text
print(response)
beautify_html = BeautifulSoup(response_html, 'lxml')

print(beautify_html)
data = {}
signin_form = beautify_html.find('form', {'name': 'signIn'})
for field in signin_form.find_all('input'):
    try:
        data[field['name']] = field['value']
    except:
        pass
data[u'email'] = "braveharambe@gmail.com"
data[u'password'] = ""
#signin
post_response = session.post('https://www.amazon.com/ap/signin', data = data)
print(post_response)

post_response = session.post('https://www.amazon.com/ga/giveaways/?pageId=1&ref_=aga_dp_lm', data = data)
print(post_response)


session.close()