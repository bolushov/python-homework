from nltk.stem import LancasterStemmer, PorterStemmer, SnowballStemmer

# Пример слов для стеммирования
words = ["running", "flies", "happily", "jumps"]

# Создаем экземпляры стеммеров
lancaster_stemmer = LancasterStemmer()
porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer("english")

# Стеммирование и вывод результатов
for word in words:
    lancaster_stem = lancaster_stemmer.stem(word)
    porter_stem = porter_stemmer.stem(word)
    snowball_stem = snowball_stemmer.stem(word)
    
    print(f"Слово: {word}, Стем (Ланскастер): {lancaster_stem}, Стем (Портер): {porter_stem}, Стем (Сноуболл): {snowball_stem}")
