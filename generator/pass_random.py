import random
import time


def password_generator():
    global user_password_length
    while True:
        try:
            # lists - ASCII
            password_digit = (el for el in map(chr, list(range(33, 127))) if el.isdigit())
            password_alpha_lower = (el for el in map(chr, list(range(97, 123))) if el.islower())
            password_alpha_upper = (el for el in map(chr, list(range(65, 91))) if el.isupper())
            password_special_characters = (el for el in '{@#}?%|*$~')

            user_password_digits = input('Настройка генератора: \n' 'Добавить числа?: y/n ').lower()
            if user_password_digits != 'y' and user_password_digits != 'n':
                raise ValueError("Допустимые значения - 'y(yes)' или 'n(no)'")

            user_small_letters = input('Добавить строчные символы?: y/n ').lower()
            if user_small_letters != 'y' and user_small_letters != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")

            user_capital_letters = input('Добавить прописные символы?: y/n ').lower()
            if user_capital_letters != 'y' and user_capital_letters != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")

            user_special_characters = input('Добавить специальные символы?: y/n ').lower()
            if user_special_characters != 'y' and user_special_characters != 'n':
                raise ValueError("Допустимые значения - 'y' или 'n'")

            while True:
                try:
                    user_password_length = int(input('Длина пароля?: '))
                    print(f'Происходит генерация пароля...')
                    time.sleep(1.5)
                    if user_password_length <= 0:
                        raise ValueError("Графа должна быть положительным числом")
                    break
                except ValueError:
                    print("Длина пароля должна быть положительным числом")
                    continue

            value_list = []
            value_list.extend(password_digit) if user_password_digits == 'y' else None
            value_list.extend(password_alpha_lower) if user_small_letters == 'y' else None
            value_list.extend(password_alpha_upper) if user_capital_letters == 'y' else None
            value_list.extend(password_special_characters) if user_special_characters == 'y' else None

            random_elements = random.choices(value_list, k=user_password_length)
            result_pass = ''.join(random_elements)
            return result_pass

        except ValueError as e:
            print(f"Ошибка: {e}\nУкажите корректные значения.\n")
            continue


def password_complexity():
    if len(result) <= 8:
        return f'Сложность пароля - Низкая'
    if 9 <= len(result) <= 14:
        return f'Сложность пароля - Средняя'
    if len(result) > 14:
        return f'Сложность пароля - Высокая'


if __name__ == '__main__':
    result = password_generator()
    print(f'Ваш пароль - {result}')
    print(password_complexity())
    with open('passwords.txt', 'a') as file:
        file.write(result + '\n')
