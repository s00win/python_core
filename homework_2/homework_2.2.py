CORRECT_PASSWORD = "Python123"
MAX_ATTEMPTS = 3

def authorize() -> bool:
    for attempt in range(1, MAX_ATTEMPTS + 1):
        password = input(f"Попытка {attempt} из {MAX_ATTEMPTS}. Введите пароль: ")

        if password == CORRECT_PASSWORD:
            print("Авторизация прошла успешно.")
            return True

        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Неверный пароль. Осталось попыток: {remaining}.")
        else:
            print("Неверный пароль.")
            return False

if __name__ == "__main__":
    if not authorize():
        print("Вход невозможен. Превышено количество попыток.")

