import random


def password_generator(*args):
    value_list = []
    if user_password_digits == 'y':
        for el in password_digit:
            value_list.append(el)
    if user_small_letters == 'y':
        for el in password_alpha_lower:
            value_list.append(el)
    if user_capital_letters == 'y':
        for el in password_alpha_upper:
            value_list.append(el)
    if user_special_characters == 'y':
        for el in password_special_characters:
            value_list.append(el)

    random_elements = random.choices(value_list, k=user_password_length)
    result = ''.join(random_elements)
    return result


# lists - ASCII
password_digit = (el for el in map(chr, list(range(33, 127))) if el.isdigit())
password_alpha_lower = (el for el in map(chr, list(range(97, 123))) if el.islower())
password_alpha_upper = (el for el in map(chr, list(range(65, 91))) if el.isupper())
password_special_characters = (el for el in '{@#}?%|*$~')

if __name__ == '__main__':
    user_password_digits = input('Настройка генератора: \n'
                                 'Добавить числа?: y/n ').lower()
    user_small_letters = input('Добавить строчные символы?: y/n ').lower()
    user_capital_letters = input('Добавить прописные символы?: y/n ').lower()
    user_special_characters = input('Добавить специальные символы?: y/n ').lower()
    user_password_length = int(input('Длина пароля?: '))
    print(password_generator())


