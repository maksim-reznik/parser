import bs4
import requests

#from urllib2 import urlopen
import requests
import sys
from bs4 import *
html = 'https://erp.uchi.ru/admin/call-request/admin/request'
session = requests.Session()
# login = raw_input('логин')
# password = raw_input('пароль')

# req = requests.get(html).text
# log = {
#     '123': login,
#     '134': password
# }
authdata = {'username': '89296617898', 'password': '12345678'}
mysession = requests.session()
response = mysession.post('https://erp.uchi.ru/admin/login', data=authdata).text
req = bs4.BeautifulSoup(response, 'html.parser')


resp = mysession.get(html, data=authdata).text
print(resp)




# resp = mysession.post('https://erp.uchi.ru/admin/call-request/admin/request', data=authdata).text
# req = bs4.BeautifulSoup(resp, 'html.parser')
# print(resp)


# mysession = requests.session()
# response = mysession.post('https://erp.uchi.ru/admin/login', data=authdata).text
# soup = BeautifulSoup(response.text,"lxml")
# print(soup)
