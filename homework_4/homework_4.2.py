INPUT_FILE = "numbers.txt"
EVEN_FILE = "even.txt"
ODD_FILE = "odd.txt"


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


def split_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]
    return evens, odds


def write_numbers(path: str, numbers: list[int]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for n in numbers:
            f.write(f"{n}\n")


if __name__ == "__main__":
    try:
        numbers = read_numbers(INPUT_FILE)
    except FileNotFoundError:
        print(f"Ошибка! Файл '{INPUT_FILE}' не найден.")
        raise SystemExit(1)

    evens, odds = split_even_odd(numbers)

    write_numbers(EVEN_FILE, evens)
    write_numbers(ODD_FILE, odds)

    print(f"Всего чисел: {len(numbers)}")
    print(f"Чётных: {len(evens)} → {EVEN_FILE}")
    print(f"Нечётных: {len(odds)} → {ODD_FILE}")
