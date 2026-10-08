FILE1 = "file_1.txt"
FILE2 = "file_2.txt"


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def swap_files(path1: str, path2: str) -> None:
    content1 = read_text(path1)
    content2 = read_text(path2)

    write_text(path1, content2)
    write_text(path2, content1)


if __name__ == "__main__":
    try:
        swap_files(FILE1, FILE2)
    except FileNotFoundError as e:
        print(f"Ошибка! Файл не найден — {e.filename}")
        raise SystemExit(1)

    print(f"Содержимое '{FILE1}' и '{FILE2}' поменялись местами.")
