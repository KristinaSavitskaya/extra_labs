equal_numbers_amount = 1

first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
third_number = int(input("Введите третье число "))

# if first_number == second_number or first_number == third_number:
#     equal_numbers_amount += 1
#     if second_number == third_number:
#         equal_numbers_amount += 1
# elif second_number == third_number:
#     equal_numbers_amount += 1
# else:
#     equal_numbers_amount = 0
# print(equal_numbers_amount)

list_numbers = [first_number, second_number, third_number]
print(list_numbers.count(first_number), list_numbers.count(second_number), list_numbers.count(third_number))

if list_numbers.count(first_number) == list_numbers.count(second_number) != 1:
    print(list_numbers.count(first_number))