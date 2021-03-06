#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


import copy
import PyPDF2
import re
import requests
import unidecode
import urllib.request
from string import punctuation
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
corpus = open("C:/Users/Dell/Desktop/bakalarka/adult TV/simply_scripts_corpus.txt", 'w+', encoding="utf-8")
website = requests.get("https://www.simplyscripts.com/tv_all.html")
html = BeautifulSoup(website.content, 'html.parser')
for link in html.find_all('a'):
	if link.get('href') != None and len(link.get('href')) > 4:
		if link.get('href')[-4:] == ".pdf":
			print(link.get('href'))
			try:
				urllib.request.urlretrieve(link.get('href'), "download.pdf")
				pdfFileObj = open('download.pdf', 'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
				for pageNum in range(pdfReader.numPages):
					pageObj = pdfReader.getPage(pageNum)
					text = pageObj.extractText()
					text = text.split('\v')
					for line in text:
						line = re.findall(r"[\w']+", line)
						for word in line:
							word = unidecode.unidecode(word)
							word = ''.join(c for c in word if (c not in punctuation) and (c != '\n') and (c != ' '))
							# if re.match(r'[A-Z][A-Z][a-z]', word):
							# re.sub(r'[A-Z]*', r'\1 ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z][A-Z]', ' ', word)
							# re.sub('[A-Z][A-Z]', ' ', word)
							if len(word) > 0:
								corpus.write(lemmatizer.lemmatize(word).lower() + " ")
				pdfFileObj.close()
			except:
				pass
corpus.close()


# In[ ]:




