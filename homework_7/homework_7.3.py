class Doctor:
    """допустим, базовый врач."""

    def treat(self) -> None:
        """Общий метод лечения. Переопределяется в наследниках."""
        print("Врач проводит общий осмотр.")


# Дочерние классы

class Surgeon(Doctor):
    """Хирург."""

    def treat(self) -> None:
        print("Хирург проводит операцию.")


class Dentist(Doctor):
    """изувер."""

    def treat(self) -> None:
        print("изувер делает больно.")


class Therapist(Doctor):
    """ТерапевтКА."""

    def treat(self) -> None:
        print("ТерапевтКА проводит прием и назначает лечение.")

    def assign_doctor(self, patient: "Patient") -> None:
        """Назначает врача пациенту по коду плана лечения и вызывает treat()."""
        # Выбираем врача по коду.
        if patient.treatment_plan == 1:
            doctor = Surgeon()
        elif patient.treatment_plan == 2:
            doctor = Dentist()
        else:
            doctor = Therapist()

        # Сохраняем врача в пациенте)))
        patient.doctor = doctor

        # Вызываем (скорую) метод лечения.
        doctor.treat()


# Класс пациента

class Patient:
    """Пациент клиники."""

    def __init__(self, treatment_plan: int):
        self.treatment_plan = treatment_plan
        self.doctor: Doctor | None = None  # врач не назначен


# Демонстрация

if __name__ == "__main__":
    print("--- Пациент с планом 1 (хирург) ---")
    p1 = Patient(treatment_plan=1)
    therapist = Therapist()
    therapist.assign_doctor(p1)
    print(f"  назначенный врач: {type(p1.doctor).__name__}\n")

    print("--- Пациент с планом 2 (дантист) ---")
    p2 = Patient(treatment_plan=2)
    therapist.assign_doctor(p2)
    print(f"  назначенный врач: {type(p2.doctor).__name__}\n")

    print("--- Пациент с планом 3 (терапевтКА) ---")
    p3 = Patient(treatment_plan=3)
    therapist.assign_doctor(p3)
    print(f"  назначенный врач: {type(p3.doctor).__name__}\n")

    # Самопроверка.
    assert isinstance(p1.doctor, Surgeon)
    assert isinstance(p2.doctor, Dentist)
    assert isinstance(p3.doctor, Therapist)
    print("Все проверки пройдены.")
