A = (input("Введите число: "))
B = (input("Введите число: "))
i = A

while True:
    try: 
        A = int(A)
        B = int(B)
        i = int(i)
        break
    except ValueError:
        print("Неверное значение")
        break

if A < B:
    while i <= B:
        print(i)
        i += 1
    count = (B-A+1)
    print(f"количество N = {count}")
else:
    print("A больше или равно B")