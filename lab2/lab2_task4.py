first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
third_number = int(input("Введите третье число "))

if first_number >= second_number:
    if first_number >= third_number:
        print(first_number)
    else:
        print(third_number)
elif second_number >= third_number:
    print(second_number)
else:
    print(third_number)
