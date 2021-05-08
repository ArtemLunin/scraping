from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

# получим все ссылки внутри страницы
# for link in bs.find_all('a'):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])

# с помощью рег. выражения получим внутренние ссылки с упоминанием К. Бейкона
for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
	if 'href' in link.attrs:
		print(link.attrs['href'])
