def book_list_view(library):
    if library:
        for book in library:
            print(f"name: {book}")
    else:
        print("Нет книг в библиотеке.")


def add_book(title, author, year):
    data = {
        "author": author,
        "year": year,
        "available": None
        }
    if title.lower() in [t.lower() for t in library]:
        print(f"Книга \"{title}\" уже есть в библиотеке. Обновить данные?")
        if input("Да/нет: ").strip().lower() == "да":
            library[title] = data
            print(f"Книга \"{title}\" обновлена.")
        else:
            print(f"Книга \"{title}\" не обновлена.")
        return

    library[title] = data
    print(f"Книга \"{title}\" добавлена в библиотеку.")


def remove_book(title):
    for real_title in library:
        if title.lower() == real_title.lower():
            library.pop(real_title)
            print(f"Книга \"{real_title}\" удалена из библиотеки")
            return
    print(f"Книга \"{title}\" не найдена в библиотеке")


def menu():
    print("""
        Возможные действия:

        1 - Добавление книги
        2 - Удаление книги
        3 - Посмотреть список книг
        q - Выход
    """)
    return input("Выберите действие: ")


def main():
    book_list_view(library)

    while True:
        match menu():
            case "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                while True:
                    try:
                        year = int(input("Введите год выхода книги: "))
                        add_book(title, author, year)
                        break
                    except ValueError:
                        print("Введите год выхода книги в \
                            формате целых чисел. Например: 1990")
            case "2":
                if not library:
                    print("Нет книг в библиотеке")
                    continue
                title = input("Введите название книги: ")
                remove_book(title)
            case "3":
                book_list_view(library)
            case "q":
                print("Программа заверщена.")
                break
            case _:
                print("Неверное действие")


library = {
    "The Lord of the Rings": {
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "available": True,
    },
    "1984": {"author": "George Orwell", "year": 1949, "available": True},
    "Moby Dick": {
        "author": "Herman Melville",
        "year": 1851,
        "available": False
        },
    "Harry Potter and the Philosopher's Stone": {
        "author": "J.K. Rowling",
        "year": 1997,
        "available": True,
    },
    "The Dark Tower": {
        "author": "Stephen King",
        "year": 1989,
        "available": True
        },
}


main()
