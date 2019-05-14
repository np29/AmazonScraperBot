from selenium import webdriver
import requests
import os

url = "https://www.amazon.com/gp/sign-in.html"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path = DRIVER_BIN)
driver.get(url)
request_cookies_browser = driver.get_cookies()

#making a persistent connection using the requests library
params = {'os_username':'braveharambe@gmail.com', 'os_password':''}
s = requests.Session()

#passing the cookies generated from the browser to the session
c = [s.cookies.set(c['name'], c['value']) for c in request_cookies_browser]

resp = s.post(url, params) #I get a 200 status_code
print(resp)
#passing the cookie of the response to the browser
dict_resp_cookies = resp.cookies.get_dict()
response_cookies_browser = [{'name':name, 'value':value} for name, value in dict_resp_cookies.items()]
c = [driver.add_cookie(c) for c in response_cookies_browser]

#the browser now contains the cookies generated from the authentication    
driver.get(url)



#session = requests.Session()

# response = session.get(url)
# response_html = response.text
# print(response)
# beautify_html = BeautifulSoup(response_html, 'lxml')

# data = {}
# signin_form = beautify_html.find('form', {'name': 'signIn'})
# for field in signin_form.find_all('input'):
#     try:
#         data[field['name']] = field['value']
#     except:
#         pass
# data[u'email'] = "braveharambe@gmail.com"
# data[u'password'] = ""
# #signin
# post_response = session.post('https://www.amazon.com/ap/signin', data = data)
# print(post_response)

# post_response = session.post('https://www.amazon.com/ga/giveaways/?pageId=1&ref_=aga_dp_lm', data = data)
# print(post_response)


#session.close()