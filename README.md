# Sprint_4
Тесты на добавление новой книги: метод add_new_book

Добавить 2 книги в self.books_genre

Добавить книгу в self.books_genre с пустым названием и с названием который содержит более 41 символа

Добавить дважды одну книгу в self.books_genre

Тесты на установку жанра для добавленой книги: метод set_book_genre

Добавить книгу в self.books_genre и присвоить ей жанр из списка self.genre

Добавить книгу в self.books_genre и присвоить ей жанр не из списка self.genre

Присвоить жанр для книги которой нету в self.books_genre

Тесты на получение жанра книги по ее имени: метод get_book_genre

Можно вывести жанр книги если добавить книгу в self.books_genre, присвоить ей жанр из списка self.genre

Если книгу не добавлять в self.books_genre список жанра книги будет пустым

Тесты на вывод списка книг с определенным жанром: метод get_books_with_specific_genre

Можно вывести список с определенным жанром если добавить книгу в self.books_genre, присвоить ей жанр из списка self.genre

Если добавить книгу в self.books_genre но не присвоить ей жанр список с определенным жанром будет пустым

Тесты на получение словаря books_genre: метод get_books_genre

Можно получить словарь books_genre если добавить книгу в self.books_genre

Можно получить словарь books_genre если добавить книгу в self.books_genre и присвоить ей жанр из списка self.genre

Если не добавлять книгу в self.books_genre словарь books_genre будет пустым

Тесты на получение списка книг подходящие детям: метод get_books_for_children

Можно получить список books_with_specific_genre если добавить книгу в self.books_genre и присвоить ей жанр из списка self.genre за исключениями которые прописаны в списке self.genre_age_rating

Если не добавить книгу или не добавить жанр или добавить жанр из списка self.genre_age_rating то список books_with_specific_genre будет пустым

Тесты на добавление книги в Избранное: метод add_book_in_favorites

Можно добавить книгу в список self.favorites если она есть в словаре self.books_genre

Книга не будет записываться в список self.favorites дважды

Тесты на удаление книги из избранного: метод delete_book_from_favorites

Можно удалить книгу из списка self.favorites если она там есть

Нельзя удалить книгу из списка self.favorites если ее там нету

Тесты на получение списка Избранных книг: метод get_list_of_favorites_books

Можно получить список self.favorites если добавить книгу в self.books_genre и в список self.favorites

Список self.favorites будет пустым если не добавлять книгу
