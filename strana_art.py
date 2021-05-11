from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

articles_link = "https://strana.ua/articles.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


def getTagValue(tagPath):
	tagValue = None
	try:
		tagValue = tagPath.strip()
	except Exception as e:
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
			# print(type(article.children))
			articleImg = None
			articleTitle = None
			articleSubTitle = None
			dateTime = None
			for articlesTags in article.children:
				# print(articlesTags.name)
				# print(articlesTags)
				try:
					print(articlesTags.div.a)
					# print(articlesTags['class'])
					if articleImg == None:
						articleImg = getTagValue(articlesTags.a.img['data-src'])
					if articleTitle == None:
						articleTitle = getTagValue(articlesTags.div.a.string)
					# if articleSubTitle == None:
					# 	articleSubTitle = getTagValue(articlesTags.div)
					if dateTime == None:
						dateTime = getTagValue(articlesTags.time.span['data-time'])
					# for realTag in articlesTags.children:
					# 	try:
					# 		# print(realTag)
					# 		# if realTag['class'][0] == 'date':
					# 		# 	print(realTag['class'][0])
					# 		# 	print(realTag.contents[1]['data-time'])
					# 		# 	print(realTag.contents[0])
					# 		# print(realTag)
					# 		print('-' * 5)
					# 	except Exception as e:
					# 			pass
				# 	ahref = articlesTags.find('div', {'class': 'lenta-text'})
				# 	# print(type(ahref))
				# 	# print(ahref)
				except AttributeError as error:
					print('Attribute error:', end='')
					print(error)
				except Exception as e:
					print('Other error:', end='')
					print(e)
			print(articleImg)
			print(articleTitle)
			print(articleSubTitle)
			print(dateTime)
			print('-' * 10)
			# s = ''.join(e for e in article if type(e) is bs4.element.NavigableString)
			# print(article)
			# print(article.a.get_text())
			# articleTitle = article.select('a.article').get_text()
			# print(articleTitle)
			print('-' * 30)
			break
	except AttributeError as error:
		print('Attribute error:', end='')
		print(error)
	except Exception as e:
		print('Other error:', end='')
		print(e)

getArticleInfo(articles_link)
