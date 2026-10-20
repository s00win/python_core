import functools


def retry(count: int):
    """Декоратор повторяет функцию до count раз, пока она не вернёт True.

    Перед каждой попыткой печатает её номер.
    """
    if not isinstance(count, int) or isinstance(count, bool):
        raise ValueError(
            f"count должен быть целым числом, получено {type(count).__name__}"
        )
    if count <= 0:
        raise ValueError(f"count должен быть положительным, получено {count}")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_result = None

            for attempt in range(1, count + 1):
                print(f"[{func.__name__}] Попытка {attempt} из {count}")
                last_result = func(*args, **kwargs)

                if last_result is True:
                    print(f"[{func.__name__}] Успех на {attempt}")
                    return True

            print(f"[{func.__name__}] Все {count} попыток исчерпаны, результата True нет")
            return last_result

        return wrapper

    return decorator


_call_counter = {"n": 0}


@retry(5)
def flaky_test():
    """Успешен с 3-й попытки."""
    _call_counter["n"] += 1
    print(f"  → выполнение теста, вызов #{_call_counter['n']}")
    return _call_counter["n"] >= 3


@retry(3)
def always_fail():
    return False


@retry(4)
def login_attempt(username, password, *, max_tries_notice=None):
    """Успешна, только если username == 'admin' и password == 'secret'."""
    print(f"  → попытка входа: {username!r} / {password!r}")
    return username == "admin" and password == "secret"


if __name__ == "__main__":
    print("--- flaky_test (успех на 3-й) ---")
    result = flaky_test()
    print(f"Итог: {result}\n")

    print("--- always_fail (все попытки мимо) ---")
    result = always_fail()
    print(f"Итог: {result}\n")

    print("--- login_attempt (успех сразу) ---")
    result = login_attempt("admin", password="secret")
    print(f"Итог: {result}\n")

    print("--- login_attempt (успех не наступит) ---")
    result = login_attempt("guest", password="wrong")
    print(f"Итог: {result}")
