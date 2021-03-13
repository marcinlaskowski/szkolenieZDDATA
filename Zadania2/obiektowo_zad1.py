"""
Utwórz klasę Książka, która ma przechować informacje na temat: tytułu, ilości stron, autora, cenę i posiadać metody:
a) wypisującą informacje: tytuł, autor i cena
b) podwyższającą cenę ksiązki o podany w parametrze procent

"""


class Book:

    def __init__(self, title, pages_number, author, price):
        self.title = title
        self.pages_number = pages_number
        self.author = author
        self.price = price

    def get_details(self):
        return f'{self.title} {self.author} - {self.price}'

    def increase_price(self, percent):
        self.price *= (1 + percent / 100)


if __name__ == "__main__":
    book = Book("Harry Potter", 130, "J.K. Rowling", 20)
    print(book.get_details())
    print(book.price)
    book.increase_price(50)
    print(book.price)
