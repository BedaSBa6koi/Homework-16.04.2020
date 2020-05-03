# Функция которая высчитывает являются ли введённые числа чётными или нет. Выводится в двух разных списках

def counting():
    digits = list(map(int, input('Enter the numbers ').split()))
    # digits = int
    odd = []
    even = []
    for i in digits:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print('Нечётные числа - ', odd)
    print('Чётные числа - ', even)
counting()





