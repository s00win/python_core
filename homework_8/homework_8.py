from __future__ import annotations


# Базовый класс цветка

class Flower:
    """Базовый цветок: название, цена, время жизни в часах."""

    def __init__(self, name: str, price: float, lifespan_hours: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название цветка должно быть непустой строкой")
        if not isinstance(price, (int, float)) or isinstance(price, bool) or price < 0:
            raise ValueError(f"Цена должна быть неотрицательным числом, получено {price!r}")
        if not isinstance(lifespan_hours, (int, float)) or isinstance(lifespan_hours, bool) or lifespan_hours <= 0:
            raise ValueError(f"Время жизни должно быть положительным, получено {lifespan_hours!r}")

        self._name = name.strip()
        self._price = float(price)
        self._lifespan_hours = float(lifespan_hours)

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def lifespan_hours(self) -> float:
        return self._lifespan_hours

    def describe(self) -> str:
        """Полиморфный метод: каждый подкласс может описать себя по-своему."""
        return f"{self._name} — {self._price:.2f}₽, живёт ~{self._lifespan_hours:.0f}ч"

    def __str__(self) -> str:
        return self.describe()

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(name={self._name!r}, "
            f"price={self._price}, lifespan_hours={self._lifespan_hours})"
        )


# Конкретные виды цветов

class Rose(Flower):
    """Роза. По умолчанию белая, привет Юре Шатунову."""

    DEFAULT_PRICE = 150.0
    DEFAULT_LIFESPAN = 72.0

    def __init__(self, color: str = "белая", name: str = "Роза",
                 price: float | None = None, lifespan_hours: float | None = None):
        super().__init__(
            name,
            price if price is not None else self.DEFAULT_PRICE,
            lifespan_hours if lifespan_hours is not None else self.DEFAULT_LIFESPAN,
        )
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    def describe(self) -> str:
        return (
            f"{self._name} ({self._color}) — {self._price:.2f}₽, "
            f"живёт ~{self._lifespan_hours:.0f}ч"
        )


class Tulip(Flower):
    """Тюльпанчик."""

    DEFAULT_PRICE = 90.0
    DEFAULT_LIFESPAN = 48.0

    def __init__(self, color: str = "желтый", name: str = "Тюльпан",
                 price: float | None = None, lifespan_hours: float | None = None):
        super().__init__(
            name,
            price if price is not None else self.DEFAULT_PRICE,
            lifespan_hours if lifespan_hours is not None else self.DEFAULT_LIFESPAN,
        )
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    def describe(self) -> str:
        return (
            f"{self._name} ({self._color}) — {self._price:.2f}₽, "
            f"живёт ~{self._lifespan_hours:.0f}ч"
        )


class Chrysanthemum(Flower):
    """Хризантема. Живёт долго — до 2 недель и даже больше."""

    DEFAULT_PRICE = 70.0
    DEFAULT_LIFESPAN = 336.0  # 14 суток

    def __init__(self, name: str = "Хризантема",
                 price: float | None = None, lifespan_hours: float | None = None):
        super().__init__(
            name,
            price if price is not None else self.DEFAULT_PRICE,
            lifespan_hours if lifespan_hours is not None else self.DEFAULT_LIFESPAN,
        )


class Orchid(Flower):
    """Орхидея — премиальный цветок."""

    DEFAULT_PRICE = 400.0
    DEFAULT_LIFESPAN = 500.0

    def __init__(self, name: str = "Орхидея",
                 price: float | None = None, lifespan_hours: float | None = None):
        super().__init__(
            name,
            price if price is not None else self.DEFAULT_PRICE,
            lifespan_hours if lifespan_hours is not None else self.DEFAULT_LIFESPAN,
        )


# Аксессуары

class Accessory:
    """Базовый аксессуар: название и цена."""

    def __init__(self, name: str, price: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название аксессуара должно быть непустой строкой")
        if not isinstance(price, (int, float)) or isinstance(price, bool) or price < 0:
            raise ValueError(f"Цена аксессуара должна быть неотрицательной, получено {price!r}")
        self._name = name.strip()
        self._price = float(price)

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    def __str__(self) -> str:
        return f"{self._name} — {self._price:.2f}₽"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self._name!r}, price={self._price})"


class Ribbon(Accessory):
    def __init__(self, price: float = 30.0):
        super().__init__("Лента", price)


class Wrapping(Accessory):
    def __init__(self, price: float = 80.0):
        super().__init__("Упаковка", price)


class Card(Accessory):
    def __init__(self, price: float = 20.0):
        super().__init__("Открытка", price)


# Букет (цветы и аксессуары)

class Bouquet:
    """Букет — сборка цветов и аксессуаров."""

    def __init__(self, name: str = "Букет"):
        self._name = name
        self._flowers: list[Flower] = []
        self._accessories: list[Accessory] = []

    # свойства
    @property
    def name(self) -> str:
        return self._name

    @property
    def flowers(self) -> list[Flower]:
        # Возвращаем копию, чтобы снаружи не могли менять внутренний список
        return list(self._flowers)

    @property
    def accessories(self) -> list[Accessory]:
        return list(self._accessories)

    # добавление
    def add_flower(self, flower: Flower) -> Bouquet:
        if not isinstance(flower, Flower):
            raise TypeError(f"Ожидался Flower, получено {type(flower).__name__}")
        self._flowers.append(flower)
        return self

    def add_accessory(self, accessory: Accessory) -> Bouquet:
        if not isinstance(accessory, Accessory):
            raise TypeError(f"Ожидался Accessory, получено {type(accessory).__name__}")
        self._accessories.append(accessory)
        return self

    # Расчёты
    def total_cost(self) -> float:
        """Общая стоимость: сумма цены цветов + аксессуаров."""
        flowers_cost = sum(f.price for f in self._flowers)
        accessories_cost = sum(a.price for a in self._accessories)
        return flowers_cost + accessories_cost

    def average_lifespan_hours(self) -> float:
        """Среднее время жизни цветов в букете (в часах). 0 — если цветов нет."""
        if not self._flowers:
            return 0.0
        return sum(f.lifespan_hours for f in self._flowers) / len(self._flowers)

    def wilting_time_hours(self) -> float:
        """Время увядания букета = среднее время жизни цветов."""
        return self.average_lifespan_hours()

    # Сортировка
    def sorted_by_price(self) -> list[Flower]:
        """Возвращает новый список цветов, отсортированный по цене."""
        return sorted(self._flowers, key=lambda f: f.price)

    def sort_by_price(self) -> Bouquet:
        """Сортирует цветы в букете по цене (на месте)."""
        self._flowers.sort(key=lambda f: f.price)
        return self

    # Поиск
    def has_flower(self, name: str) -> bool:
        """Есть ли в букете цветок с таким названием (без учёта регистра)."""
        if not isinstance(name, str):
            return False
        return any(f.name.lower() == name.lower() for f in self._flowers)

    def __contains__(self, name: str) -> bool:
        """Позволяет писать: 'Роза' in bouquet"""
        return self.has_flower(name)

    # Магические методы
    def __len__(self) -> int:
        return len(self._flowers)

    def __iter__(self):
        return iter(self._flowers)

    def __str__(self) -> str:
        lines = [f"Букет «{self._name}» ({len(self._flowers)} цветов):"]

        lines.append("  Цветы:")
        if self._flowers:
            for f in self._flowers:
                lines.append(f"    - {f.describe()}")
        else:
            lines.append("    (пусто)")

        if self._accessories:
            lines.append("  Аксессуары:")
            for a in self._accessories:
                lines.append(f"    - {a}")

        lines.append(f"  Общая стоимость: {self.total_cost():.2f}₽")
        lines.append(f"  Время увядания (среднее): {self.wilting_time_hours():.1f}ч")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return (
            f"Bouquet(name={self._name!r}, "
            f"flowers={len(self._flowers)}, accessories={len(self._accessories)})"
        )


# Демонстрация

if __name__ == "__main__":
    bouquet = Bouquet("")

    # Собираем букет из разных цветов
    bouquet.add_flower(Rose(color="красная"))  # 150
    bouquet.add_flower(Rose(color="белая", price=170))  # 170
    bouquet.add_flower(Tulip(color="жёлтый"))  # 90
    bouquet.add_flower(Chrysanthemum())  # 70
    bouquet.add_flower(Orchid())  # 400

    # Добавляем аксессуары
    bouquet.add_accessory(Ribbon())  # 30
    bouquet.add_accessory(Wrapping())  # 80
    bouquet.add_accessory(Card())  # 20

    print(bouquet)
    print()

    # Проверки
    print("Сортировка по цене (возвращает новый список):")
    for f in bouquet.sorted_by_price():
        print(f"  {f.price:>6.2f}₽  {f.name}")

    print("\nПроверка наличия цветка:")
    print(f"  'Роза' в букете?      {'Роза' in bouquet}")
    print(f"  'Ромашка' в букете?   {'Ромашка' in bouquet}")

    print("\nСортировка на месте и вывод:")
    bouquet.sort_by_price()
    for f in bouquet:
        print(f"  {f.name} — {f.price:.2f}₽")

    # Самопроверки
    assert bouquet.total_cost() == 150 + 170 + 90 + 70 + 400 + 30 + 80 + 20  # 1010
    assert bouquet.average_lifespan_hours() == (72 + 72 + 48 + 336 + 500) / 5
    assert "Роза" in bouquet
    assert "Орхидея" in bouquet
    assert "Ромашка" not in bouquet
    assert [f.price for f in bouquet.sorted_by_price()] == sorted([f.price for f in bouquet])
    print("\nВсе проверки пройдены.")
