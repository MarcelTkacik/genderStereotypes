#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import nltk

def clean(word):
	output = ""
	for char in word:
		if char == '[' or char == ']' or char == '{' or char == '}':
			pass
		else:
			output += char
	return output

file_count = 0
writefile_all = open("C:/Users/Dell/Desktop/bakalarka/clean data/adult clean speech/adult_speech_corpus.txt", 'w+', encoding="utf-8")
for (root,dirs,files) in os.walk("C:/Users/Dell/Desktop/bakalarka/raw data/adult raw speech", topdown=True):
	for file in files:
		if file[-9:] == 'word.text':
			print(file)
			output = ""
			readfile = open(os.path.join(root,file), "r")
			for line in readfile:
				words = line.split()
				word = str(words[-1:][0]).lower()
				if word[0] == '[':
					word = word[1:-1]
				if word[:9] == 'laughter-':
					word = word[9:]
				elif word[:8] == "silence-":
					word = word[8:]
				elif word[:6] == "noise-":
					word = word[6:]
				word = clean(word)
				if word[-2:] == "_1":
					word = word[:-2]
				if word[0] == '-':
					word = word[1:]
				if word == "silence" or word == "noise" or word == "laughter":
					pass
				elif word[-1:] == "-":
					pass
				elif word[0] == '<':
					pass
				else:
					output += word + " "
			writefile_all.write(output)
			readfile.close()
writefile_all.close()

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
file = open("C:/Users/Dell/Desktop/bakalarka/clean data/adult clean speech/adult_speech_corpus.txt", 'r', encoding="utf-8")
outfile = open("C:/Users/Dell/Desktop/bakalarka/clean data/adult clean speech/lemmatized_adult_speech_corpus.txt", 'w+', encoding="utf-8")
words = file.read().split()
for word in words:
	outfile.write(lemmatizer.lemmatize(word.lower()) + " ")
outfile.close()
file.close()


# In[ ]:




