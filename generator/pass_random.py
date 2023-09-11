import random
import time


def generate_password():
    password_symbols = {
        'digit': ''.join(map(str, range(10))),
        'alpha_lower': 'abcdefghijklmnopqrstuvwxyz',
        'alpha_upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'special_characters': '{@#}?%|*$~'
    }

    while True:
        try:
            user_password_digits = input('Добавить числа? [y/N]: ').lower()
            if user_password_digits != 'y' and user_password_digits != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue

    while True:
        try:
            user_small_letters = input('Добавить строчные символы? [y/N]: ').lower()
            if user_small_letters != 'y' and user_small_letters != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue

    while True:
        try:
            user_capital_letters = input('Добавить прописные символы? [y/N]: ').lower()
            if user_capital_letters != 'y' and user_capital_letters != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue

    while True:
        try:
            user_special_characters = input('Добавить специальные символы? [y/N]: ').lower()
            if user_special_characters != 'y' and user_special_characters != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue

    value_list = []
    if user_password_digits == 'y':
        value_list.extend(password_symbols['digit'])
    if user_small_letters == 'y':
        value_list.extend(password_symbols['alpha_lower'])
    if user_capital_letters == 'y':
        value_list.extend(password_symbols['alpha_upper'])
    if user_special_characters == 'y':
        value_list.extend(password_symbols['special_characters'])

    if len(value_list) == 0:
        print('Пожалуйста, выберите один из вариантов')
        time.sleep(1)
        return generate_password()

    while True:
        try:
            user_password_length = int(input('Длина пароля?: '))
            if user_password_length <= 0:
                raise ValueError('Длина пароля должна быть положительным числом')
            print(f'Происходит генерация пароля...')
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue

    random_elements = random.choices(value_list, k=user_password_length)
    result_pass = ''.join(random_elements)
    time.sleep(2)
    return result_pass


def assess_password_complexity(password):
    if len(password) <= 8:
        return f'Сложность пароля - Низкая'
    if 9 <= len(password) <= 14:
        return f'Сложность пароля - Средняя'
    if len(password) > 14:
        return f'Сложность пароля - Высокая'


def save_password(password):
    try:
        while True:
            retention_request = input('Сохранить пароль в файл? [y/N]: ')
            if retention_request != 'y' and retention_request != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")
            if retention_request == 'y':
                with open('passwords.txt', 'a') as file:
                    file.write(password + '\n')
                time.sleep(1)
                print(f'Пароль - {password} сохранен в "passwords.txt"')
            else:
                time.sleep(0.5)
                print('До новых встреч!')
            break

    except ValueError:
        time.sleep(0.5)
        print("Допустимые значения - 'y' или 'n'")
        save_password(password)


if __name__ == '__main__':
    password = generate_password()
    print(f'Ваш пароль - {password}')
    print(assess_password_complexity(password))
    save_password(password)
