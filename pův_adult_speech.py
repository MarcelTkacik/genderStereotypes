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
writefile_all = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/Adult_Speech/adult_speech_corpus.txt", 'w+')
for (root,dirs,files) in os.walk("/Users/tessacharlesworth/Desktop/Embeddings/Raw Data/Adult_Speech/Adult raw speech", topdown=True):
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
file = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/Adult_Speech/adult_speech_corpus.txt", 'r')
outfile = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/Adult_Speech/lemmatized_adult_speech_corpus.txt", 'w+')
words = file.read().split()
for word in words:
	outfile.write(lemmatizer.lemmatize(word.lower()) + " ")
outfile.close()
file.close()