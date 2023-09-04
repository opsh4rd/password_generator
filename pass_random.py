import random

user_password_digits = input('Добавить в генерацию числа y/n: ').lower()
user_small_letters = input('Добавить в генерацию строчные символы y/n: ').lower()
user_capital_letters = input('Добавить в генерацию прописные символы y/n: ').lower()
user_special_characters = input('Добавить в генерацию специальные символы y/n: ').lower()
user_password_length = int(input('Укажите длинну пароля: '))

password_digits = [random.randint(1, 10) for el in range(user_password_length)]
print(password_digits)
