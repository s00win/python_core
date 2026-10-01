import random
import string

STATUSES = ("ACTIVE", "BLOCKED", "INACTIVE")

MIN_AGE = 18
MAX_AGE = 65

LOGIN_LENGTH = 8


def generate_login() -> str:
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits,
                                    k=LOGIN_LENGTH))
    return f"user_{suffix}"


def generate_age() -> int:
    return random.randint(MIN_AGE, MAX_AGE)


def generate_status() -> str:
    return random.choice(STATUSES)


def generate_user() -> dict:
    return {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status(),
    }


if __name__ == "__main__":
    print("Пример сгенерированного пользователя:")
    print(generate_user())
