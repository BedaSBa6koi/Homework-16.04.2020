# Функция проверяющая является ли слово палиндромом

def palindrome():
    word = input('Enter the word ')
    word = word.lower()
    if str(word) == str(word)[::-1]:
        print(True)
    else:
        print(False)
palindrome()


