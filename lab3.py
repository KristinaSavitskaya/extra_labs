is_continued = True

def function_sum(a: float, b: float) -> float:
    return a + b

def function_subtraction(a: float, b: float) -> float:
    return a - b

def function_multiplication(a: float, b: float) -> float:
    return a * b

def function_division(a: float, b: float) -> int:
    return int(a // b)

def function_factorial(a: int) -> int:
    answer = 1
    for i in range(1, a+1):
        answer = answer * i
    return answer

def not_number(a) -> bool:
    if (a.replace(".", "")).isnumeric():
        return False
    else:
        return True

while is_continued:
    print("There are 5 available mathematical operations:")
    print("1. a + b \n2. a - b \n3. a * b \n4. a // b \n5. a!\n6. Exit")
    operation = input("Pick the mathematical operation as a number: ")

    if operation not in ["1", "2", "3", "4", "5", "6"]:
        print("You need to enter a number from 1 to 6")
        continue
    
    if int(operation) == 6:
        is_continued = False
        continue

    elif int(operation) == 5:
        a = input("Enter your number: ")
        while not_number(a):
            a = input("Please enter a number: ")

        answer = function_factorial(int(a))
    
    else:
        a = input("Enter your first number: ")
        while not_number(a):
            a = input("Please enter a number: ")

        b = input("Enter your second number: ")
        while not_number(b):
            b = input("Please enter a number: ")

        if int(operation) == 1:
            answer = function_sum(float(a), float(b))
        elif int(operation) == 2:
            answer = function_subtraction(float(a), float(b))
        elif int(operation) == 3:
            answer = function_multiplication(float(a), float(b))
        elif int(operation) == 4:
            answer = function_division(float(a), float(b))

    print(f"Your answer is {answer}")
    print()