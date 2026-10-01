VALID_STATUS = ("PASS", "FAIL", "SKIP")


def get_test_statistics(results: list[str]) -> dict:
    stats = {"PASS": 0, "FAIL": 0, "SKIP": 0, "total": 0}

    for raw in results:
        status = raw.strip().upper()
        if status not in VALID_STATUS:
            continue
        stats[status] += 1
        stats["total"] += 1

    return stats


def print_report(stats: dict) -> None:
    total = stats["total"]
    print(f"Всего тестов: {total}")
    print(f"PASS: {stats['PASS']}")
    print(f"FAIL: {stats['FAIL']}")
    print(f"SKIP: {stats['SKIP']}")

    if total == 0:
        print("Успешно: 0.0%")
    else:
        success_percent = stats["PASS"] / total * 100
        print(f"Успешно: {success_percent:.1f}%")


if __name__ == "__main__":
    line = input("Введите результаты тестов через пробел: ")
    results = line.split()

    stats = get_test_statistics(results)
    print_report(stats)
