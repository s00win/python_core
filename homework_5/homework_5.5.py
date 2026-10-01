import json
from functools import reduce

INPUT_FILE = "test_results.json"
OUTPUT_FILE = "report.json"

VALID_STATUSES = ("PASS", "FAIL", "SKIP")
REQUIRED_FIELDS = ("name", "status", "duration")


class InvalidTestDataError(Exception):
    """Поднимается, когда структура тестовых данных некорректна."""


def load_tests(path: str) -> list[dict]:
    """Читает JSON-файл с тестами и валидирует структуру.

    Поднимает:
      - FileNotFoundError — если файл не найден;
      - json.JSONDecodeError — если содержимое не JSON;
      - InvalidTestDataError — если структура данных неверна.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise InvalidTestDataError(
            f"Ожидался список тестов, получено {type(data).__name__}"
        )

    for i, test in enumerate(data, start=1):
        if not isinstance(test, dict):
            raise InvalidTestDataError(
                f"Тест №{i} — не объект (получено {type(test).__name__})"
            )
        missing = [f for f in REQUIRED_FIELDS if f not in test]
        if missing:
            raise InvalidTestDataError(
                f"Тест №{i} ('{test.get('name', '?')}'): "
                f"отсутствуют поля: {', '.join(missing)}"
            )
        if test["status"] not in VALID_STATUSES:
            raise InvalidTestDataError(
                f"Тест №{i} ('{test['name']}'): недопустимый статус "
                f"{test['status']!r}. Ожидался один из: {', '.join(VALID_STATUSES)}"
            )
        if not isinstance(test["duration"], (int, float)) or test["duration"] < 0:
            raise InvalidTestDataError(
                f"Тест №{i} ('{test['name']}'): duration должно быть "
                f"неотрицательным числом, получено {test['duration']!r}"
            )

    return data


def count_by_status(tests: list[dict]) -> dict:
    """Возвращает словарь со счётчиками по каждому статусу."""
    statuses = [t["status"] for t in tests]
    return {status: statuses.count(status) for status in VALID_STATUSES}


def get_failed_tests(tests: list[dict]) -> list[dict]:
    """filter() + lambda — список упавших тестов (объекты целиком)."""
    return list(filter(lambda t: t["status"] == "FAIL", tests))


def get_failed_names(tests: list[dict]) -> list[str]:
    """filter() + lambda + генератор — только названия упавших."""
    failed = filter(lambda t: t["status"] == "FAIL", tests)
    return [t["name"] for t in failed]


def get_longest_test(tests: list[dict]) -> dict | None:
    """Самый длительный тест. lambda + max()."""
    if not tests:
        return None
    longest = max(tests, key=lambda t: t["duration"])
    return {"name": longest["name"], "duration": longest["duration"]}


def total_duration(tests: list[dict]) -> float:
    """reduce() + lambda — суммарное время выполнения."""
    return reduce(lambda acc, t: acc + t["duration"], tests, 0.0)


def build_report(tests: list[dict]) -> dict:
    """Собирает итоговый отчёт в виде словаря."""
    return {
        "total": len(tests),
        "counts": count_by_status(tests),
        "failed_tests": get_failed_names(tests),
        "longest_test": get_longest_test(tests),
        "total_duration": round(total_duration(tests), 2),
    }


def save_report(report: dict, path: str) -> None:
    """Сохраняет отчёт в JSON-файл."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    try:
        tests = load_tests(INPUT_FILE)
        report = build_report(tests)
        save_report(report, OUTPUT_FILE)
    except FileNotFoundError as e:
        print(f"Ошибка! Файл '{e.filename}' не найден.")
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        print(f"Ошибка! Невалидный JSON в '{INPUT_FILE}'.")
        print(f"  Строка {e.lineno}, колонка {e.colno}: {e.msg}")
        raise SystemExit(1)
    except InvalidTestDataError as e:
        print(f"Ошибка структуры данных: {e}")
        raise SystemExit(1)
    except PermissionError as e:
        print(f"Ошибка! Нет доступа к файлу '{e.filename}'.")
        raise SystemExit(1)

    print(f"Отчёт сохранён в '{OUTPUT_FILE}'.")
    print(f"Всего тестов: {report['total']}")
    print(f"Упавших: {report['counts']['FAIL']}")
    print(f"Общее время: {report['total_duration']} с")
