import os
import tempfile

from src.main import save_to_file


def test_save_to_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    content = "Тест"
    save_to_file(filename, content)

    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

    assert data == content

    os.remove(filename)
