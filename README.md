# qa_python
1. test_add_new_book_invalid_book_name - проверка, что книги с невалидным названием (пустая и длинная строки) не добавляются в books_genre
2. test_init_default_genre_true - проверка, что в созданном объекте есть дефолтный список жанров
3. test_set_book_genre_genre_not_in_genre - проверка, что несуществующий жанр нельзя установить
4. test_get_book_genre_true - проверка, что получаем жанр книги по имени
5. test_get_books_with_specific_genre_true - проверка, что получаем список книг по жанру
6. test_get_books_genre_true - проверка, что получаем словарь books_genre
7. test_get_books_for_children_age_rating_not_for_children - проверка, что книги с жанрами возрастного рейтинга не попадают в список детских книг
8. test_add_book_in_favorites_book_not_in_books_genre - проверка, что нельзя добавить в избранное книгу, которой нет в books_genre
9. test_delete_book_from_favorites_true - проверка, что книга удаляется из избранного
10. test_get_list_of_favorites_books_true - проверка, что получаем список избранных книг
