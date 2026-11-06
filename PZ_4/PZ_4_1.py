"""Даны два целых числа А и В (А < В). Вывести в порядке возрастания все целые числа, расположенные между А и В (включая сами числа А и В),
 а также количество N этих чисел"""


A = (input("Введите число: "))
B = (input("Введите число: "))
i = A

while True:             # Проверка
    try: 
        A = int(A)
        B = int(B)
        i = int(i)
        break
    except ValueError:
        print("Неверное значение")
        break

if A < B:                # Условие
    while i <= B:
        print(i)
        i += 1
    count = (B-A+1)
    print(f"количество N = {count}")
else:
    print("A больше или равно B")
    print()