school = {
    "1а": 25,
    "1б": 27,
    "2а": 24,
    "3б": 26,
    "5в": 30,
    "6а": 28,
    "7в": 22,
    "9а": 19,
    "10б": 21,
    "11а": 18,
}

print("Школа:")
for klass, count in school.items():
    print(f" Класс {klass}: {count} учеников")

print("\nВсего классов:", len(school))
print("Всего учеников:", sum(school.values()))