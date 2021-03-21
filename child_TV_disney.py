#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib3
import requests
import re
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from string import punctuation

lemmatizer = WordNetLemmatizer()
corpus = open("C:/Users/Dell/Desktop/bakalarka/child TV/disney_corpus.txt", 'w+')
website = requests.get("http://transcripts.wikia.com/wiki/Category:Disney")
html = BeautifulSoup(website.content, 'html.parser')
count = 0
num_tv_shows = 0
for link in html.find_all('a'):
	episodes = 0
	lnk = link.get('href')
	if lnk != None:
		if lnk[:6] == "/wiki/" and lnk[6:14] != "Special:" and lnk[6:14] != "Category" and lnk[6:17] != "Transcripts":
			count += 1
			if count > 21:
				print(lnk)
				print("---")
				page = requests.get("http://transcripts.wikia.com" + lnk)
				soup = BeautifulSoup(page.content, 'html.parser')
				counter = 0
				for episode in soup.find_all('a'):
					episode_link = episode.get('href')
					if episode_link != None:
						if (episode_link[:6] == "/wiki/" and "action=" not in episode_link and 
							episode_link[6:14] != "Special:" and episode_link[6:14] != "Category" and 
							episode_link[6:17] != "Transcripts" and episode_link[6:] != "Captain_America:_Civil_War" and 
							episode_link[6:] != "Local_Sitemap" and episode_link[6:] != "Avengers:_Age_of_Ultron" and 
							episode_link[6:] != "Avengers:_Infinity_War"):
							counter += 1
							if counter > 18:
								print(episode_link)
								episodes = 1
								subpage = requests.get("http://transcripts.wikia.com" + episode_link)
								subsoup = BeautifulSoup(subpage.content, 'html.parser')
								if subsoup.find(class_="mw-content-ltr mw-content-text"):
									transcript = subsoup.find(class_="mw-content-ltr mw-content-text").get_text()
									num_tv_shows += 1
									for text in transcript.split('\n'):
										for word in text.split():
											word = re.sub(r'[^\w]', '', word)#.join(c for c in word if (c not in punctuation) and (c != '\n'))
											if len(word) > 0:
												corpus.write(" " + lemmatizer.lemmatize(word).lower())
				if episodes == 0:
					if soup.find(class_="mw-content-ltr mw-content-text"):
						transcript = soup.find(class_="mw-content-ltr mw-content-text").get_text()
						num_tv_shows += 1
						for text in transcript.split('\n'):
							for word in text.split():
								word = re.sub(r'[^\w]', '', word)#.join(c for c in word if (c not in punctuation) and (c != '\n'))
								if len(word) > 0:
									corpus.write(" " + lemmatizer.lemmatize(word).lower())
				print("------")
corpus.close()
print(num_tv_shows)


# In[ ]:




