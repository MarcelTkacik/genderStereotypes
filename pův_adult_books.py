from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from nltk.stem import WordNetLemmatizer
from string import punctuation
import random

lemmatizer = WordNetLemmatizer()
corpus = open("/Users/tessacharlesworth/Desktop/Embeddings/Clean Data/Adult_Books/gutenberg_corpus.txt", 'w+')
count = 0
sampled = random.sample(range(1,60000),1000) # change "1000" to the total number of books desired.
for i in sampled:
	text_test = 1
	try:
		text = strip_headers(load_etext(i)).strip()
	except Exception:
		text_test = 0
	if text_test == 1:
		for word in text.split():
			word = ''.join(c for c in word if c not in punctuation)
			corpus.write(lemmatizer.lemmatize(word.lower()) + " ")
		print("Completed " + str(i))
		count += 1
	if count % 100 == 0:
		print(count)
corpus.close()