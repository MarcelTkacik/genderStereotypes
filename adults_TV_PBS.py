#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib3
import requests
import html2text
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from string import punctuation

lemmatizer = WordNetLemmatizer()
corpus = open("C:/Users/Dell/Desktop/bakalarka/adult TV/pbs_adults_corpus.txt", 'w+', encoding="utf-8")
webpages = []
website1 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_anth.html")
webpages.append(BeautifulSoup(website1.content, 'html.parser'))
website2 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_disa.html")
webpages.append(BeautifulSoup(website2.content, 'html.parser'))
website3 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_eart.html")
webpages.append(BeautifulSoup(website3.content, 'html.parser'))
website4 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_expl.html")
webpages.append(BeautifulSoup(website4.content, 'html.parser'))
website5 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_flig.html")
webpages.append(BeautifulSoup(website5.content, 'html.parser'))
website6 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_heal.html")
webpages.append(BeautifulSoup(website6.content, 'html.parser'))
website7 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_hist.html")
webpages.append(BeautifulSoup(website7.content, 'html.parser'))
website8 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_inve.html")
webpages.append(BeautifulSoup(website8.content, 'html.parser'))
website9 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_natu.html")
webpages.append(BeautifulSoup(website9.content, 'html.parser'))
website10 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_phys.html")
webpages.append(BeautifulSoup(website10.content, 'html.parser'))
website11 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_spac.html")
webpages.append(BeautifulSoup(website11.content, 'html.parser'))
website12 = requests.get("http://www.pbs.org/wgbh/nova/transcripts/int_tech.html")
webpages.append(BeautifulSoup(website12.content, 'html.parser'))
h = html2text.HTML2Text()
h.ignore_links = True

counter = 0
for link in webpages:
	print(link.title.string)
	for lnk in link.find_all('a'):
		subpage = requests.get("http://www.pbs.org" + (lnk).get('href'))
		if lnk.get('href') == "/wgbh/nova/transcripts/alph_a.html":
			break
		if lnk.get('href')[:23] == "/wgbh/nova/transcripts/" and len(lnk.get('href')) > 23:
			print(lnk.get('href'))
			counter += 1
			response = requests.get("http://www.pbs.org" + (lnk).get('href'))
			soup = BeautifulSoup(response.content, "html.parser")
			i = 0
			text = soup.find_all('p')[i].get_text()
			while text != None:
				text.rstrip()
				text.lstrip()
				texts = text.split('\n')
				for txt in texts:
					txt = txt.split()
					for word in txt:
						word = ''.join(c for c in word if (c not in punctuation) and (c != '\n'))
						if len(word) > 0:
							corpus.write(lemmatizer.lemmatize(word).lower() + " ")
				i += 1
				if len(soup.find_all('p')) > i:
					text = soup.find_all('p')[i].get_text()
				else:
					break
	print("-----")
corpus.close()
print(counter)


# In[2]:





# In[ ]:




