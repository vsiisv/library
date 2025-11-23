def book_list_view(library):
    if library:
        for book in library:
            print(f"name: {book}")
    else:
        print("Нет книг в библиотеке.")


def add_book(title, author, year):
    if title in library:
        print(f"Книга {title} уже есть в библиотеке. Обновить данные?")
        if input("Да/нет: ") == "Да".lower():
            library[title] = {"author": author, "year": year, "available": None}
            print(f"Книга {title} обновлена.")
        else:
            print(f"Книга {title} не обновлена.")
            return

    else:
        library[title] = {"author": author, "year": year, "available": None}
        print(f"Книга {title} добавлена в библиотеку.")
        return


library = {
    "The Lord of the Rings": {
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "available": True,
    },
    "1984": {"author": "George Orwell", "year": 1949, "available": True},
    "Mobie Dick": {"author": "Herman Melville", "year": 1851, "available": False},
    "Harry Potter and the Philosopher's Stone": {
        "author": "J.K. Rowling",
        "year": 1997,
        "available": True,
    },
    "Harry Potter and the Chamber of Secrets": {
        "author": "J.K. Rowling",
        "year": 1998,
        "available": True,
    },
    "Harry Potter and the Prisoner of Azkaban": {
        "author": "J.K. Rowling",
        "year": 1999,
        "available": False,
    },
    "Harry Potter and the Goblet of Fire": {
        "author": "J.K. Rowling",
        "year": 2000,
        "available": True,
    },
    "Harry Potter and the Order of the Phoenix": {
        "author": "J.K. Rowling",
        "year": 2003,
        "available": True,
    },
    "Harry Potter and the Half-Blood Prince": {
        "author": "J.K. Rowling",
        "year": 2005,
        "available": False,
    },
    "Harry Potter and the Deathly Hallows": {
        "author": "J.K. Rowling",
        "year": 2007,
        "available": True,
    },
    "V": {"author": "Thomas Pynchon", "year": 1963, "available": True},
    "Robinson Crusoe": {"author": "Daniel Defoe", "year": 1719, "available": False},
    "The Holy Flower": {"author": "H. Rider Haggard", "year": 1905, "available": True},
    "IT": {"author": "Stephen King", "year": 1986, "available": True},
    "The Mist": {"author": "Stephen King", "year": 1980, "available": False},
    "The Long Walk": {"author": "Stephen King", "year": 1979, "available": True},
    "The Game of Thrones": {
        "author": "George R.R. Martin",
        "year": 1996,
        "available": True,
    },
    "Dune": {"author": "Frank Herbert", "year": 1965, "available": False},
    "The Shining": {"author": "Stephen King", "year": 1977, "available": True},
    "The Running Man": {"author": "Stephen King", "year": 1987, "available": True},
    "Institute": {"author": "Stephen King", "year": 1991, "available": True},
    "The Stand": {"author": "Stephen King", "year": 1978, "available": True},
    "Tom Sawyer": {"author": "Mark Twain", "year": 1876, "available": False},
    "Mutant 59: The Plastic Eater": {
        "author": "Kit Pedler",
        "year": 1971,
        "available": True,
    },
    "The Dark Tower": {"author": "Stephen King", "year": 1989, "available": True},
    "Gekkle Sky": {"author": "Stephen King", "year": 1982, "available": True},
    "The Dark Half": {"author": "Stephen King", "year": 1995, "available": True},
    "The Eye of the World": {"author": "Stephen King", "year": 1991, "available": True},
}


def main():
    book_list_view(library)
    print()
    if input("Добавить новую книгу? (Да/нет): ") == "Да".lower():
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год выхода книги: ")

        add_book(title, author, year)
    else:
        print("Книга не добавлена.")


main()
