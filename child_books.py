#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk
## when installing nltk, you will also need to install "wordnet" using nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
file = open("C:/Users/Dell/Desktop/bakalarka/raw data/childes raw books/child_books.txt", 'r')
outfile = open("C:/Users/Dell/Desktop/bakalarka/clean data/childes clean books/lemmatized_child_books.txt", 'w+')
words = file.read().split()
for word in words:
	if ((word.find('_') != -1) or (word.find('.') != -1) or (word.find(':') != -1) or (word.find(';') != -1) or
		(word.find('?') != -1) or (word.find('`') != -1) or (word.find('!') != -1) or (word.find(',') != -1) or
		(word.find('-') != -1) or word == 'CHAPTER' or not word.isalnum()):
		pass
	else:
		outfile.write(lemmatizer.lemmatize(word).lower() + " ")
print(len(words))
outfile.close()
file.close()


# In[ ]:


5548143


# In[ ]:




