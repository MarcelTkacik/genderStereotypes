import os
import nltk
from nltk.corpus.reader import CHILDESCorpusReader

corpus_root = nltk.data.find('/Users/tessacharlesworth/Desktop/Embeddings/Raw Data/CHILDES raw text/') # change to local directory where the raw text files are stored
childes = CHILDESCorpusReader(corpus_root,'\S*.xml')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

file_count = 0
writefile_children = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/CHILDES clean text/corpus_children.txt", 'w+') # change to local directory where the combined text files should be stored; keep "corpus_children.txt", 'w+'" at the end
for (root,dirs,files) in os.walk("/Users/tessacharlesworth/Desktop/Embeddings/Raw Data/CHILDES raw text/", topdown=True): # change to local directory where the raw text files are stored
	for file in files:
		if file[-4:] == '.xml':
				print(file)
				output = childes.words(os.path.join(root,file),speaker=['CHI'],replace=True)
				output = list(filter(lambda a: a != 'xxxxxxxx', output))
				output = list(filter(lambda a: a != 'xxxxxxx', output))
				output = list(filter(lambda a: a != 'xxxxxx', output))
				output = list(filter(lambda a: a != 'xxxxx', output))
				output = list(filter(lambda a: a != 'xxxx', output))
				output = list(filter(lambda a: a != 'xxx', output))
				output = list(filter(lambda a: a != 'xx', output))
				output = list(filter(lambda a: a != 'yyy', output))
				output = list(filter(lambda a: a != 'yy', output))
				output = (' '.join(output)).lower()
				writefile_children.write(output)
				file_count += 1

writefile_children.close()
print(file_count)
file = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/CHILDES clean text/corpus_children.txt", 'r')
outfile = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/CHILDES clean text/lemmatized_corpus_children.txt", 'w+')
words = file.read().split()
for word in words:
	outfile.write(lemmatizer.lemmatize(word.lower()) + " ")
outfile.close()
file.close()

file_count = 0
writefile_parents = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/CHILDES clean text/corpus_parents.txt", 'w+')
for (root,dirs,files) in os.walk("/Users/tessacharlesworth/Desktop/Embeddings/Raw Data/CHILDES raw text/", topdown=True): # change to local directory where the raw text files are stored
	for file in files:
		if file[-4:] == '.xml':
				output = childes.words(os.path.join(root,file),speaker=['MOT','FAT'],replace=True)
				output = list(filter(lambda a: a != 'xxxxxxxx', output))
				output = list(filter(lambda a: a != 'xxxxxxx', output))
				output = list(filter(lambda a: a != 'xxxxxx', output))
				output = list(filter(lambda a: a != 'xxxxx', output))
				output = list(filter(lambda a: a != 'xxxx', output))
				output = list(filter(lambda a: a != 'xxx', output))
				output = list(filter(lambda a: a != 'xx', output))
				output = list(filter(lambda a: a != 'yyy', output))
				output = list(filter(lambda a: a != 'yy', output))
				output = (' '.join(output)).lower()
				writefile_parents.write(output)
				file_count += 1
writefile_parents.close()
print(file_count)
file = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/CHILDES clean text/corpus_parents.txt", 'r')
outfile = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/CHILDES clean text/lemmatized_corpus_parents.txt", 'w+')
words = file.read().split()
for word in words:
	outfile.write(lemmatizer.lemmatize(word.lower()) + " ")
outfile.close()
file.close()