FILENAME = "flt_numbers.txt"
PRECISION = 6  # количество значащих цифр при выводе


def read_numbers(path: str) -> list[float]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    numbers = []
    for token in text.split():
        try:
            numbers.append(float(token))
        except ValueError:
            print(f"Предупреждение! '{token}' — не число, пропущено.")
    return numbers


def square(numbers: list[float]) -> list[float]:
    return [x * x for x in numbers]


def write_numbers(path: str, numbers: list[float]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for x in numbers:
            f.write(f"{x:.{PRECISION}g}\n")


def replace_with_squares(path: str) -> None:
    numbers = read_numbers(path)
    squared = square(numbers)
    write_numbers(path, squared)


if __name__ == "__main__":
    try:
        replace_with_squares(FILENAME)
    except FileNotFoundError:
        print(f"Ошибка! Файл '{FILENAME}' не найден.")
        raise SystemExit(1)

    print(f"Файл '{FILENAME}' обновлён, все числа возведены в квадрат.")
