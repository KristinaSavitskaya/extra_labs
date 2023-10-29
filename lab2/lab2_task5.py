equal_numbers_amount = 1

first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
third_number = int(input("Введите третье число "))

if first_number == second_number or first_number == third_number:
    equal_numbers_amount += 1
    if second_number == third_number:
        equal_numbers_amount += 1
elif second_number == third_number:
    equal_numbers_amount += 1
else:
    equal_numbers_amount = 0
print(equal_numbers_amount)
