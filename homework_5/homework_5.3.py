MIN_RETRIES = 0
MAX_RETRIES = 5


def run_test(retries: int, timeout: float) -> str:
    if not isinstance(retries, int) or isinstance(retries, bool):
        raise ValueError(
            f"retries должно быть целым числом, получено "
            f"{type(retries).__name__}: {retries!r}"
        )
    if not (MIN_RETRIES <= retries <= MAX_RETRIES):
        raise ValueError(
            f"retries должно быть в диапазоне "
            f"{MIN_RETRIES}..{MAX_RETRIES}, получено {retries}"
        )

    if not isinstance(timeout, (int, float)) or isinstance(timeout, bool):
        raise ValueError(
            f"timeout должно быть числом, получено "
            f"{type(timeout).__name__}: {timeout!r}"
        )
    if timeout <= 0:
        raise ValueError(
            f"timeout должен быть положительным, получено {timeout}"
        )

    return (
        f"Тест запущен: повторных попыток = {retries}, "
        f"таймаут = {timeout} с"
    )


def run_scenario(name: str, retries, timeout) -> None:
    print(f"--- {name} ---")
    try:
        result = run_test(retries, timeout)
        print(f"OK. {result}")
    except ValueError as e:
        print(f"ОШИБКА! {e}")
    print()


if __name__ == "__main__":
    run_scenario("Корректные значения", retries=3, timeout=2.5)

    run_scenario("Отрицательный таймаут", retries=2, timeout=-1.0)

    run_scenario("Слишком много повторов", retries=10, timeout=1.0)

    run_scenario("Ноль повторных запусков", retries=0, timeout=0.1)
    run_scenario("Нулевой таймаут", retries=1, timeout=0)
    run_scenario("Нецелое число повторов", retries=2.5, timeout=1.0)
