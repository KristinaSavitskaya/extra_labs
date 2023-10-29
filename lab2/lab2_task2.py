lesson_number = int(input("Номер урока "))
minutes = lesson_number*45 + (lesson_number-1)*5 + (lesson_number-1)//2 * 10
print("Урок закончится в", 9 + minutes // 60, minutes % 60)