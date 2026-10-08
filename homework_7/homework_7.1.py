class CreditCard:
    """Кредитная карта с номером счёта и балансом."""

    def __init__(self, account: str, initial_balance: float = 0.0):
        """Создаёт карту.

        account — номер счёта (непустая строка).
        initial_balance — начальный баланс (неотрицательное число).
        """
        # Валидация входных данных.
        if not isinstance(account, str) or not account.strip():
            raise ValueError("account должен быть непустой строкой")

        if not isinstance(initial_balance, (int, float)) or isinstance(initial_balance, bool):
            raise ValueError("initial_balance должен быть числом")

        if initial_balance < 0:
            raise ValueError("initial_balance не может быть отрицательным")

        # Сохраняем в атрибуты экземпляра.
        self._account = account.strip()
        self._balance = float(initial_balance)

    # Публичные методы

    def deposit(self, amount: float) -> float:
        """Пополняет баланс на amount. Возвращает новый баланс."""
        self._validate_amount(amount)
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Снимает amount со счёта. Возвращает новый баланс.

        Если средств недостаточно — поднимает ValueError.
        """
        self._validate_amount(amount)

        if amount > self._balance:
            raise ValueError(
                f"Недостаточно средств на счёте {self._account}: "
                f"запрошено {amount}, доступно {self._balance}"
            )

        self._balance -= amount
        return self._balance

    def show_info(self) -> None:
        """Печатает номер счёта и текущий баланс."""
        print(f"Счёт: {self._account} | Баланс: {self._balance:.2f}")

    # Свойства (для удобного чтения)

    @property
    def account(self) -> str:
        return self._account

    @property
    def balance(self) -> float:
        return self._balance

    # Вспомогательные

    def _validate_amount(self, amount) -> None:
        """Проверяет, что сумма операции положительное число."""
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError(f"amount должен быть числом, получено {type(amount).__name__}")
        if amount <= 0:
            raise ValueError(f"amount должен быть положительным, получено {amount}")

    # Магические методы

    def __repr__(self) -> str:
        return f"CreditCard(account={self._account!r}, balance={self._balance})"

    def __str__(self) -> str:
        return f"Счёт {self._account}: {self._balance:.2f}"


# Демонстрация

if __name__ == "__main__":
    # Создаём три карты с разными счетами и балансами.
    card1 = CreditCard("ACC-001", 1000.0)
    card2 = CreditCard("ACC-002", 2500.5)
    card3 = CreditCard("ACC-003", 300.0)

    # Операции:
    card1.deposit(500.0)  # пополнил первую
    card2.deposit(1500.0)  # пополнил вторую
    card3.withdraw(200.0)  # снял с третьей

    # Выводим информацию о всех трёх картах.
    print("Состояние карт после операций:")
    print("-" * 40)
    card1.show_info()
    card2.show_info()
    card3.show_info()
    print("-" * 40)

    # Проверки для самоконтроля.
    assert card1.balance == 1500.0
    assert card2.balance == 4000.5
    assert card3.balance == 100.0
    print("Все проверки пройдены.")
