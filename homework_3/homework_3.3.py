import random

TESTS = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search",
]

STATUSES = ("PASS", "FAIL", "SKIP")


def read_count(prompt: str, max_count: int) -> int | None:
    raw = input(prompt).strip()

    if not raw.isdigit() or int(raw) == 0:
        print(f"Ошибка! Введите положительное целое число.")
        return None

    count = int(raw)

    if count > max_count:
        print(f"Ошибка! В списке только {max_count} тестов, "
              f"нельзя запустить {count}.")
        return None

    return count


def generate_run(count: int) -> dict:
    selected = random.sample(TESTS, k=count)
    return {name: random.choice(STATUSES) for name in selected}


def print_report(results: dict) -> bool:
    pass_count = fail_count = skip_count = 0

    print("\nОтчёт о запуске тестов:")
    for name, status in results.items():
        print(f"{name} — {status}")
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1
        else:
            skip_count += 1

    total = len(results)
    print()
    print(f"Всего запущено: {total}")
    print(f"PASS: {pass_count}")
    print(f"FAIL: {fail_count}")
    print(f"SKIP: {skip_count}")

    if fail_count > 0:
        print("Запуск неуспешный (есть упавшие тесты).")
        return False

    print("Запуск успешный.")
    return True


if __name__ == "__main__":
    count = read_count(
        f"Сколько тестов запустить? (1–{len(TESTS)}): ",
        max_count=len(TESTS),
    )

    if count is None:
        raise SystemExit(1)

    results = generate_run(count)
    print_report(results)
