from nltk.stem import PorterStemmer

# Создаем экземпляр стеммера
stemmer = PorterStemmer()
words = ["running", "flies", "happily", "jumps"]
# Стеммирование  слов
for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"Слово: {word}, Стем: {stemmed_word}")
