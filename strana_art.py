from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

url_site = "https://strana.ua"
articles_link = url_site + "/articles.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


def getTagValue(tagPath):
	tagValue = None
	try:
		tagValue = tagPath.strip()
	except Exception as e:
		print('fail...')
		pass
	return tagValue

pages = set()
def getArticleInfo(pageUrl):
	global pages
	req = Request(url=pageUrl, headers=headers)
	html = urlopen(req)
	bsObj = BeautifulSoup(html, "html.parser")
	try:
		articles = bsObj.find_all('article', {'class': 'lenta-news'})
		for article in articles:
			articleImg = getTagValue(article.find('img')['data-src'])
			articleTitle = getTagValue(article.find('a', {'class': 'article'}).contents[0])
			articleHREF = url_site + getTagValue(
				article.find('a', {'class': 'article'})['href'])
			articleSubTitle = getTagValue(article.find(
				'div', {'class': 'subtitle'}).contents[0])
			dateTime = getTagValue(article.find(
				'span', {'class': 'strana-adate'})['data-time'])
			print('Article Link:' + articleHREF)
			print('Image link:' + articleImg)
			print('Title:' + articleTitle)
			print('Subtitle:' + articleSubTitle)
			print('Date:' + dateTime)
			print('-' * 30)
	except AttributeError as error:
		pass
	except Exception as e:
		print('Other error:', end='')
		print(e)

getArticleInfo(articles_link)
