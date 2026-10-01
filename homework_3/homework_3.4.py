from homework_3.user_generation import test_data


def read_count(prompt: str, max_count: int) -> int | None:
    raw = input(prompt).strip()

    if not raw.isdigit() or int(raw) == 0:
        print("Ошибка! Введите положительное целое число.")
        return None

    count = int(raw)
    if count > max_count:
        print(f"Ошибка! За один раз можно сгенерировать не больше {max_count}.")
        return None

    return count


def generate_users(count: int) -> list[dict]:
    return [test_data.generate_user() for _ in range(count)]


def print_users(users: list[dict]) -> None:
    print("\nСгенерированные пользователи:")
    for i, user in enumerate(users, start=1):
        print(f"  {i}. {user['login']} | возраст: {user['age']} | статус: {user['status']}")


def print_stats(users: list[dict]) -> None:
    stats = {status: 0 for status in test_data.STATUSES}

    for user in users:
        stats[user["status"]] += 1

    print("\nСтатистика по статусам:")
    for status, count in stats.items():
        print(f"  {status}: {count}")

    print(f"  Всего: {len(users)}")


if __name__ == "__main__":
    count = read_count("Сколько пользователей сгенерировать? (1–100): ", max_count=100)
    if count is None:
        raise SystemExit(1)

    users = generate_users(count)
    print_users(users)
    print_stats(users)
