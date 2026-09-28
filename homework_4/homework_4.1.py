FILENAME = "numbers.txt"


def read_numbers(path: str) -> list[int]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    numbers = []
    for token in text.split():
        try:
            numbers.append(int(token))
        except ValueError:
            print(f"Предупреждение! '{token}' — не число, пропускаем.")
    return numbers


def print_extremes(numbers: list[int]) -> None:
    print(f"Первый элемент:        {numbers[0]}")
    print(f"Второй элемент:        {numbers[1]}")
    print(f"Предпоследний элемент: {numbers[-2]}")
    print(f"Последний элемент:     {numbers[-1]}")


if __name__ == "__main__":
    try:
        numbers = read_numbers(FILENAME)
    except FileNotFoundError:
        print(f"Ошибка! Файл '{FILENAME}' не найден.")
        raise SystemExit(1)

    if len(numbers) < 3:
        print(f"Ошибка! В файле только {len(numbers)} чисел, "
              f"нужно минимум 3 числа.")
        raise SystemExit(1)

    print(f"Всего чисел в файле:   {len(numbers)}")
    print_extremes(numbers)
