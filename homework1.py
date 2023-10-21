print('Здравствуйте, заполните анкету, где вам будут предложены несколько вопросов:')

first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
birth_year = int(input("Введите ваш год рождения: "))
movie_genre = input("Какой ваш любимый жанр фильмов? ")
movie_name = input("Какой был последний просмотренный вами фильм? ")

age = 2023 - birth_year
full_name = first_name + " " + last_name

print("\nВы ввели следующие ответы:")

print("Вас зовут", full_name)
print(f"Вам {age} лет")
print("Ваш любимый жанр фильмов:", movie_genre)
print("Последний просмотренный вами фильм:", movie_name)