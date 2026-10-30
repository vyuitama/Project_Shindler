"""Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его
Вывести полученное число"""
num = int(input("Введите целое число\n"))
while True:
    try:
        num = int(num)
        break
    except ValueError:
        print("Error")

if num >= 0:
    num += 1
print(num)

