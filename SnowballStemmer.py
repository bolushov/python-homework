from nltk.stem import SnowballStemmer

# Выберите язык, для которого вы хотите использовать стеммер
language = "english"  # Пример для английского языка
stemmer = SnowballStemmer(language)

# Пример слов для стеммирования
words = ["running", "flies", "happily", "jumps"]

# Стеммирование каждого слова и вывод результатов
for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"Слово: {word}, Стем: {stemmed_word}")
