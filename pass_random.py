# import random

user_password_digits = input('Настройка генератора: \n'
                             'Добавить числа?: y/n ').lower()
user_small_letters = input('Добавить строчные символы?: y/n ').lower()
user_capital_letters = input('Добавить прописные символы?: y/n ').lower()
user_special_characters = input('Добавить специальные символы?: y/n ').lower()
user_password_length = int(input('Длина пароля?: '))

# lists - ASCII
password_digit = [el for el in map(chr, list(range(33, 127))) if el.isdigit()]
password_alpha_lower = [el for el in map(chr, list(range(97, 123))) if el.islower()]
password_alpha_upper = [el for el in map(chr, list(range(65, 91))) if el.upper()]
password_special_characters = [el for el in '{@#}?%|*$~']
