def count_pass(tests: list) -> int:
    """Рекурсивно считает количество тестов со статусом PASS.

    Использует только рекурсию: ни for, ни while, ни sum().
    """
    if not tests:
        return 0

    head, tail = tests[0], tests[1:]
    if head == "PASS":
        return 1 + count_pass(tail)
    return count_pass(tail)


if __name__ == "__main__":
    results = [
        "PASS", "FAIL", "PASS", "SKIP", "PASS",
        "FAIL", "PASS", "SKIP", "PASS",
    ]

    print(f"Всего тестов: {len(results)}")
    print(f"PASS-тестов: {count_pass(results)}")

    assert count_pass([]) == 0
    assert count_pass(["PASS"]) == 1
    assert count_pass(["FAIL"]) == 0
    assert count_pass(results) == 5
    print("Все проверки пройдены.")
