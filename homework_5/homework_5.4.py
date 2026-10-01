class InvalidTestStatusError(Exception):
    """Поднимается, когда статус теста не PASS, FAIL или SKIP."""


VALID_STATUSES = ("PASS", "FAIL", "SKIP")


def validate_status(status) -> str:
    """Проверяет статус теста.

    Возвращает статус, если он корректен.
    Иначе поднимает InvalidTestStatusError.
    """
    if status not in VALID_STATUSES:
        raise InvalidTestStatusError(
            f"Недопустимый статус теста: {status!r}. "
            f"Допустимы только: {', '.join(VALID_STATUSES)}."
        )
    return status


if __name__ == "__main__":
    for s in ("PASS", "FAIL", "SKIP", "pass", "UNKNOWN"):
        try:
            result = validate_status(s)
        except InvalidTestStatusError as e:
            print(f"ОШИБКА! {e}")
        else:
            print(f"OK. статус '{result}' принят.")