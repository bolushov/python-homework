from nltk.stem import LancasterStemmer
stemmer = LancasterStemmer()
words = ["running", "flies", "happily", "jumps"]
for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"Слово: {word}, Стем: {stemmed_word}")
