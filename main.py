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
print(response)