import functools


def log_test(func):
    """Декоратор для логирования автотестов.

    Печатает имя теста перед запуском, результат после выполнения
    и сообщение о завершении.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[START] {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[RESULT] {func.__name__} → {result!r}")
        print(f"[END] {func.__name__}")

        return result

    return wrapper


@log_test
def test_login(username, password):
    """Проверяет авторизацию пользователя."""
    return "success" if password == "secret" else "fail"


@log_test
def test_payment(amount, currency="RUB", **meta):
    """Проверяет оплату с произвольными дополнительными параметрами."""
    return f"paid {amount} {currency}"


@log_test
def test_ping():
    """Простейший тест без аргументов."""
    return "pong"


if __name__ == "__main__":
    test_login("admin", "secret")
    print()
    test_login(username="guest", password="wrong")
    print()
    test_payment(100, currency="USD", comment="test")
    print()
    test_ping()

    print()
    print("Метаданные test_login:")
    print(f"  __name__: {test_login.__name__}")
    print(f"  __doc__:  {test_login.__doc__}")
