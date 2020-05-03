#Функция, которая сортирует положительные и отрицательные числа в имеющимся уже списке

def sorting():
    a = [48, -3242, 344, 11, 34, 43, 678, -1, -2, 23, -32, 0]
    
    print (a)
    
    b = []
    c = []
    for i in a:
        if i < 0:
            b.append(i)
        else:
            c.append(i)

    print(b)
    print(c)
    input('To start the next function, press Enter\n')
sorting()        


#Функция, которая сортирует положительные и отрицательные числа введённые пользователем

def sorting_input():
    a = list(map(int, input('Enter positive and negative numbers ').split()))
    
    b = []
    c = []
    for i in a:
        if i < 0:
            b.append(i)
        else:
            c.append(i)

    print(b)
    print(c)
sorting_input() 
   
    
