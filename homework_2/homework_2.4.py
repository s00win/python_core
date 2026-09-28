SECRET = 37

def guess_number() -> int:
    attempts = 0

    while True:
        raw = input("Введите число: ")
        if not raw.lstrip("-").isdigit():
            print("Введите целое число.")
            continue
        guess = int(raw)
        attempts += 1
        if guess == SECRET:
            print(f"Вы угадали. Использовано попыток : {attempts}.")
            break
        elif guess < SECRET:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    return attempts

if __name__ == "__main__":
    guess_number()