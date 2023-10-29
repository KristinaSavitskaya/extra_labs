a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

list_numbers = [a, b, c]
list_numbers.sort()
a, b, c = list_numbers[0], list_numbers[1], list_numbers[2]
print(a, b, c)