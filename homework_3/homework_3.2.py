test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]


def print_report(test_cases: list[str], statuses: list[str]) -> bool:
    if len(test_cases) != len(statuses):
        print("Предупреждение: длина списков не совпадает, "
              "будут выведены только общие пары.")

    pass_count = 0
    fail_count = 0

    print("Отчёт о запуске тестов:")
    for name, status in zip(test_cases, statuses):
        print(f"{name} — {status}")

        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1

    print()
    print(f"Успешных тестов: {pass_count}")
    print(f"Неуспешных тестов: {fail_count}")

    if fail_count > 0:
        print("Запуск неуспешный (есть упавшие тесты).")
        return False

    print("Запуск успешный.")
    return True


if __name__ == "__main__":
    success = print_report(test_cases, statuses)
