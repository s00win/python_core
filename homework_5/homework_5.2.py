import json

FILENAME = "users.json"
REQUIRED_FIELDS = ("login", "password", "expected")


def load_users(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(
            f"Ожидался список пользователей, получено {type(data).__name__}"
        )

    for i, user in enumerate(data):
        if not isinstance(user, dict):
            raise ValueError(f"Пользователь №{i + 1} — не объект (dict)")
        missing = [field for field in REQUIRED_FIELDS if field not in user]
        if missing:
            raise KeyError(
                f"У пользователя №{i + 1} отсутствуют поля: {', '.join(missing)}"
            )

    return data


def print_users(users: list[dict]) -> None:
    print(f"Всего пользователей: {len(users)}\n")
    for i, user in enumerate(users, start=1):
        print(f"Пользователь №{i}")
        print(f"  Логин:             {user['login']}")
        print(f"  Пароль:            {user['password']}")
        print(f"  Ожидаемый итог:    {user['expected']}")
        print()


if __name__ == "__main__":
    try:
        users = load_users(FILENAME)
    except FileNotFoundError as e:
        print(f"Ошибка: файл '{e.filename}' не найден.")
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        print(f"Ошибка: невалидный JSON в файле '{FILENAME}'.")
        print(f"  Строка {e.lineno}, колонка {e.colno}: {e.msg}")
        raise SystemExit(1)
    except KeyError as e:
        # args[0] — сообщение, которое мы передали в KeyError.
        print(f"Ошибка структуры данных: {e.args[0]}")
        raise SystemExit(1)
    except ValueError as e:
        print(f"Ошибка структуры данных: {e}")
        raise SystemExit(1)
    except PermissionError as e:
        print(f"Ошибка: нет доступа к файлу '{e.filename}'.")
        raise SystemExit(1)

    print_users(users)
