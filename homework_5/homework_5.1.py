from functools import reduce
from collections import Counter

STATUSES = ("PASS", "FAIL", "SKIP")

tests = [
    {"name": "test_login", "status": "PASS", "duration": 1.25},
    {"name": "test_logout", "status": "FAIL", "duration": 0.80},
    {"name": "test_registration", "status": "PASS", "duration": 2.10},
    {"name": "test_profile", "status": "SKIP", "duration": 0.00},
    {"name": "test_payment", "status": "FAIL", "duration": 3.45},
    {"name": "test_search", "status": "PASS", "duration": 1.90},
]


def get_failed_names(tests: list[dict]) -> list[str]:
    failed = filter(lambda t: t["status"] == "FAIL", tests)
    return list(map(lambda t: t["name"], failed))


def get_passed_names(tests: list[dict]) -> list[str]:
    return [t["name"] for t in tests if t["status"] == "PASS"]


def total_duration(tests: list[dict]) -> float:
    return reduce(lambda acc, t: acc + t["duration"], tests, 0.0)


def count_by_status(tests: list[dict]) -> dict:
    counter = Counter(t["status"] for t in tests)
    return {status: counter.get(status, 0) for status in STATUSES}


def print_report(tests: list[dict]) -> None:
    counts = count_by_status(tests)
    failed = get_failed_names(tests)
    passed = get_passed_names(tests)
    total = total_duration(tests)

    print("Статистика по статусам:")
    for status in STATUSES:
        print(f"  {status}: {counts[status]}")

    print(f"\nУпавшие тесты ({len(failed)}):")
    for name in failed:
        print(f"  - {name}")

    print(f"\nУспешные тесты ({len(passed)}):")
    for name in passed:
        print(f"  - {name}")

    print(f"\nОбщее время выполнения: {total:.2f} с")


if __name__ == "__main__":
    print_report(tests)
