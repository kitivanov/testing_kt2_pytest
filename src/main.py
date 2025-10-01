def string_length(s: str) -> int:
    """Возвращает длину строки."""
    return len(s)


def save_to_file(filename: str, content: str) -> None:
    """Сохраняет строку в файл."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
