def create_time_checker(max_time: float):
    """Возвращает функцию-чекер, которая проверяет, уложился ли тест в лимит.

    max_time — максимально допустимое время выполнения (секунды).
    """
    if max_time <= 0:
        raise ValueError(f"max_time должен быть положительным, получено {max_time}")

    def check(actual_time: float) -> str:
        """Проверяет фактическое время относительно лимита max_time."""
        if actual_time <= max_time:
            return f"OK. {actual_time} с ≤ {max_time} с"
        return f"ПРЕВЫШЕНИЕ. {actual_time} с > {max_time} с"

    return check


if __name__ == "__main__":
    fast_check = create_time_checker(1.0)
    slow_check = create_time_checker(5.0)

    test_times = [0.5, 1.0, 2.5, 4.9, 5.0, 7.2]

    print(f"{'Время':>6} | {'fast_check (≤1с)':<25} | {'slow_check (≤5с)':<25}")
    print("-" * 70)
    for t in test_times:
        print(f"{t:>6} | {fast_check(t):<25} | {slow_check(t):<25}")

    assert "OK" in fast_check(0.5)
    assert "ПРЕВЫШЕНИЕ" in fast_check(2.0)
    assert "OK" in slow_check(3.0)
    assert "ПРЕВЫШЕНИЕ" in slow_check(10.0)

    print()
    print(f"fast_check помнит лимит: {fast_check(0.9)}")
    print(f"slow_check помнит лимит: {slow_check(0.9)}")
