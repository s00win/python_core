class ATM:
    """Банкомат с купюрами номиналом 100, 50 и 20."""

    DENOMINATIONS = (100, 50, 20)

    def __init__(self, count_100: int = 0, count_50: int = 0, count_20: int = 0):
        self._bills = {
            100: self._validate_count(count_100, 100),
            50: self._validate_count(count_50, 50),
            20: self._validate_count(count_20, 20),
        }

    # Публичные методы

    def add_money(self, count_100: int = 0, count_50: int = 0, count_20: int = 0) -> None:
        """Добавляет купюры каждого номинала. Пропущенные номиналы не меняются."""
        self._bills[100] += self._validate_count(count_100, 100)
        self._bills[50] += self._validate_count(count_50, 50)
        self._bills[20] += self._validate_count(count_20, 20)

    def withdraw(self, amount: int) -> bool:
        """Пытается выдать сумму. Возвращает True, если удалось,
        и False, если выдать нельзя (состояние не меняется)."""
        # Проверка входных данных.
        if not isinstance(amount, int) or isinstance(amount, bool):
            return False
        if amount <= 0 or amount % 10 != 0:
            return False

        # Поиск комбинации купюр.
        combination = self._find_combination(amount)
        if combination is None:
            return False

        n100, n50, n20 = combination

        # Фиксируем, списываем купюры.
        self._bills[100] -= n100
        self._bills[50] -= n50
        self._bills[20] -= n20

        # Печатаем, что выдали, и возвращаем True.
        print(f"Выдано {amount}: {n100}×100, {n50}×50, {n20}×20")
        return True

    def show_info(self) -> None:
        """Печатает текущее состояние банкомата."""
        b = self._bills
        print(
            f"ATM: 100 — {b[100]}, 50 — {b[50]}, 20 — {b[20]} "
            f"(всего купюр: {sum(b.values())}, сумма: {self.total})"
        )

    @property
    def total(self) -> int:
        """Общая сумма денег в банкомате."""
        return sum(denom * count for denom, count in self._bills.items())

    # Внутренние методы

    def _find_combination(self, amount: int):
        """Ищет комбинацию (n100, n50, n20) или возвращает None.

        Идёт от максимума крупных купюр к минимуму — так находится
        решение с наибольшим числом крупных купюр.
        """
        max_100 = min(self._bills[100], amount // 100)
        for n100 in range(max_100, -1, -1):
            rest_100 = amount - n100 * 100

            max_50 = min(self._bills[50], rest_100 // 50)
            for n50 in range(max_50, -1, -1):
                rest_50 = rest_100 - n50 * 50

                # Остаток должен делиться на 20 и двадцаток должно хватить.
                if rest_50 % 20 == 0:
                    n20 = rest_50 // 20
                    if n20 <= self._bills[20]:
                        return n100, n50, n20

        return None

    @staticmethod
    def _validate_count(value, denom: int) -> int:
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(
                f"Количество купюр номинала {denom} должно быть целым, "
                f"получено {type(value).__name__}"
            )
        if value < 0:
            raise ValueError(
                f"Количество купюр номинала {denom} не может быть "
                f"отрицательным. {value}"
            )
        return value

    def __repr__(self) -> str:
        return f"ATM({self._bills})"


# Демонстрация

if __name__ == "__main__":
    # Создаём банкомат с начальным запасом купюр.
    atm = ATM(count_100=2, count_50=3, count_20=5)
    print("Изначально:")
    atm.show_info()
    print()

    # Добавим купюры.
    atm.add_money(count_100=3, count_50=2, count_20=10)
    print("После add_money(100=3, 50=2, 20=10):")
    atm.show_info()
    print()

    # Несколько операций снятия — успешных и нет.
    print(f"withdraw(380) → {atm.withdraw(380)}")
    atm.show_info()
    print()

    print(f"withdraw(60) → {atm.withdraw(60)}")
    atm.show_info()
    print()

    print(f"withdraw(15) → {atm.withdraw(15)}")  # не кратно 10
    print(f"withdraw(-50) → {atm.withdraw(-50)}")  # отрицательная
    print(f"withdraw(99999) → {atm.withdraw(99999)}")  # много
    atm.show_info()
