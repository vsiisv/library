def book_list_view(library):
    if library:
        for book in library:
            print(f"name: {book}")
    else:
        print("Нет книг в библиотеке.")


def add_book(title, author, year):
    if title.lower() in [t.lower() for t in library]:
        print(f'Книга "{title}" уже есть в библиотеке. Обновить данные?')
        if input("Да/нет: ").strip().lower() == "да":
            library[title] = {"author": author, "year": year, "available": None}
            print(f'Книга "{title}" обновлена.')
        else:
            print(f'Книга "{title}" не обновлена.')

    else:
        library[title] = {"author": author, "year": year, "available": None}
        print(f'Книга "{title}" добавлена в библиотеку.')


def main():
    book_list_view(library)
    if input("\nДобавить новую книгу? (Да/нет): ").lower() == "да":
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        while True:
            try:
                year = int(input("Введите год выхода книги: "))
                add_book(title, author, year)
                break
            except ValueError:
                print("Введите год выхода книги в формате целых чисел. Например: 1990")

    else:
        print("Книга не добавлена.")


library = {
    "The Lord of the Rings": {
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "available": True,
    },
    "1984": {"author": "George Orwell", "year": 1949, "available": True},
    "Moby Dick": {"author": "Herman Melville", "year": 1851, "available": False},
    "Harry Potter and the Philosopher's Stone": {
        "author": "J.K. Rowling",
        "year": 1997,
        "available": True,
    },
    "The Dark Tower": {"author": "Stephen King", "year": 1989, "available": True},
}


main()
