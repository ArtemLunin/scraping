from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

articles_link = "https://strana.ua/articles.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

pages = set()
def getArticleInfo(pageUrl):
	global pages
	req = Request(url=pageUrl, headers=headers)
	html = urlopen(req)
	bsObj = BeautifulSoup(html, "html.parser")
	try:
		articles = bsObj.find_all('article', {'class': 'lenta-news title'})
		for article in articles:
			# print(type(article.children))
			for articlesTags in article.children:
				print(articlesTags)
				print('-' * 10)
			# s = ''.join(e for e in article if type(e) is bs4.element.NavigableString)
			# print(article)
			# print(article.a.get_text())
			# articleTitle = article.select('a.article').get_text()
			# print(articleTitle)
			print('-' * 30)
	except:
	    print('error')

getArticleInfo(articles_link)
