VALID_STATUS = ("PASS", "FAIL", "SKIP")


def read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Введите положительное целое число.")


def collect_stats(total: int) -> dict:
    stats = {"PASS": 0, "FAIL": 0, "SKIP": 0}

    for i in range(1, total + 1):
        raw = input(f"Тест {i} из {total}. Статус (PASS/FAIL/SKIP): ")
        status = raw.strip().upper()

        if status not in VALID_STATUS:
            print(f"Статус неизвестен '{raw}'. Пропущено.")
            continue

        stats[status] += 1

    return stats


def print_report(stats: dict) -> None:
    print("\nИтоговая статистика:")
    print(f"  PASS: {stats['PASS']}")
    print(f"  FAIL: {stats['FAIL']}")
    print(f"  SKIP: {stats['SKIP']}")

    if stats["FAIL"] > 0:
        print(f"\nОбнаружены упавшие тесты: {stats['FAIL']}. Требуется разбор.")
    else:
        print("\nВсе выполненные тесты прошли успешно.")


if __name__ == "__main__":
    total = read_positive_int("Сколько выполнено тестов? ")
    statistics = collect_stats(total)
    print_report(statistics)