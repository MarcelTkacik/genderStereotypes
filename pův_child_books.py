import nltk
## when installing nltk, you will also need to install "wordnet" using nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
file = open("/Users/tessacharlesworth/Desktop/Embeddings/Raw Data/Child_Books/child_books.txt", 'r')
outfile = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/Child_Books/lemmatized_child_books.txt", 'w+')
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