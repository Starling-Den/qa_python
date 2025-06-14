import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book_name', ['', 'z' * 41])
    def test_add_new_book_invalid_book_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_init_default_genre_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_set_book_genre_genre_not_in_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Карась')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == ""

    def test_get_book_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert 'Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить' in collector.get_books_with_specific_genre('Фантастика') \
                                                   and 'Восточный экспресс' not in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Дюймовочка')
        collector.set_book_genre('Дюймовочка', 'Мультфильмы')
        assert collector.get_books_genre() == {'Дюймовочка': 'Мультфильмы' }

    def test_get_books_for_children_age_rating_not_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        assert 'Кладбище домашних животных' not in collector.get_books_for_children()

    def test_add_book_in_favorites_book_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Дюймовочка')
        assert 'Дюймовочка' not in collector.favorites

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Дюймовочка')
        collector.add_book_in_favorites('Дюймовочка')
        collector.delete_book_from_favorites('Дюймовочка')
        assert 'Дюймовочка' not in collector.favorites

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Дюймовочка')
        collector.add_book_in_favorites('Дюймовочка')
        assert 'Дюймовочка' in collector.get_list_of_favorites_books()
