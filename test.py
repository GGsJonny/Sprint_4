import pytest

class TestBooksCollector:

    # добавляем новую книгу
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Приключения Алисы в Стране чудес')
        collector.add_new_book('Тайна старого замка')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'Путешествие к центру Земли'])
    def test_add_new_book_add_books_len_name_not_in_books_genre(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_add_books_without_duplicate_books(self, collector):
        collector.add_new_book('Дракула')
        collector.add_new_book('Дракула')
        assert len(collector.books_genre) == 1

    # устанавливаем книге жанр
    def test_set_book_genre_add_book_and_set_genre(self, collector):
        collector.add_new_book('Вокруг света за 80 дней')
        collector.set_book_genre('Вокруг света за 80 дней', 'Приключения')
        assert 'Приключения' in collector.books_genre.values()

    def test_set_book_genre_add_book_and_set_non_existent_genre(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Роман')
        assert 'Роман' not in collector.books_genre.values()

    def test_set_book_genre_set_genre_not_add_book(self, collector):
        collector.set_book_genre('Франкенштейн', 'Ужасы')
        assert 'Франкенштейн' not in collector.books_genre

    # получаем жанр книги по её имени
    def test_get_book_genre_add_book_and_set_genre(self, collector):
        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Классика')
        assert collector.books_genre.get('Идиот') == 'Классика'

    def test_get_book_genre_set_genre_without_add_book(self, collector):
        collector.set_book_genre('Идиот', 'Классика')
        assert collector.books_genre.get('Идиот') is None

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_add_two_books_and_set_genre_displays_specific_genre(self, collector):
        collector.add_new_book('Собачье сердце')
        collector.add_new_book('Белый клык')
        collector.set_book_genre('Собачье сердце', 'Сатира')
        collector.set_book_genre('Белый клык', 'Приключения')
        assert collector.get_books_with_specific_genre('Сатира') == ['Собачье сердце']

    @pytest.mark.parametrize('genre', ['', 'Сатира'])
    def test_get_books_with_specific_genre_books_with_specific_genre_is_empty(self, collector, genre):
        collector.add_new_book('Собачье сердце')
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    # получаем словарь books_genre

    def test_get_books_genre_add_two_books(self, collector):
        collector.add_new_book('Собачье сердце')
        collector.add_new_book('Белый клык')
        assert collector.get_books_genre() == {'Собачье сердце': '', 'Белый клык': ''}

    def test_get_books_genre_add_two_books_and_set_books_genre(self, collector):
        collector.add_new_book('Собачье сердце')
        collector.add_new_book('Белый клык')
        collector.set_book_genre('Собачье сердце', 'Сатира')
        collector.set_book_genre('Белый клык', 'Приключения')
        assert collector.get_books_genre() == {'Собачье сердце': 'Сатира', 'Белый клык': 'Приключения'}

    def test_get_books_genre_books_genre_is_empty(self, collector):
        assert collector.get_books_genre() == {}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_add_two_books_set_children_genre(self, collector):
        collector.add_new_book('Алиса в Стране чудес')
        collector.add_new_book('Питер Пэн')
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Алиса в Стране чудес', 'Сказка')
        collector.set_book_genre('Питер Пэн', 'Сказка')
        collector.set_book_genre('Винни-Пух', 'Сказка')
        assert collector.get_books_for_children() == ['Алиса в Стране чудес', 'Питер Пэн', 'Винни-Пух']

    @pytest.mark.parametrize(
        'books_and_genres',
        [
            [('Три мушкетера', 'Приключения'), ('Джекилл и Хайд', 'Ужасы')],
            [],
            [('Колобок', '')]
        ]
    )
    def test_get_books_for_children_books_for_children_is_empty(self, collector, books_and_genres):
        for book, genre in books_and_genres:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == []

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_book_exists(self, collector):
        collector.add_new_book('Граф Монте-Кристо')
        collector.add_book_in_favorites('Граф Монте-Кристо')
        assert 'Граф Монте-Кристо' in collector.favorites

    def test_add_book_in_favorites_duplicate_book(self, collector):
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        assert collector.favorites.count('Унесенные ветром') == 1

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_book_exists(self, collector):
        collector.add_new_book('Мёртвые души')
        collector.add_book_in_favorites('Мёртвые души')
        collector.delete_book_from_favorites('Мёртвые души')
        assert 'Мёртвые души' not in collector.favorites

    def test_delete_book_from_favorites_book_not_exists(self, collector):
        collector.add_new_book('Мёртвые души')
        collector.add_book_in_favorites('Мёртвые души')
        collector.delete_book_from_favorites('Котики')
        assert 'Мёртвые души' in collector.favorites

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_book_exists(self, collector):
        collector.add_new_book('Остров сокровищ')
        collector.add_book_in_favorites('Остров сокровищ')
        assert collector.get_list_of_favorites_books() == ['Остров сокровищ']

    def test_get_list_of_favorites_books_is_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []

