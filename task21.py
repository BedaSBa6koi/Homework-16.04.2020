# Функция для вывода самого длинного слова из введённых

def maxlen():
    words = input('Enter the sentence ').split()
    words = max(words, key=len)
    print(words)
maxlen()

