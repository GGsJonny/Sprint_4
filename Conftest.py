import pytest

from main import BooksCollector

# Фикстура для BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()