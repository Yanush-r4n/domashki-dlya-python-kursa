def show_data() -> None:
    """Выводит информацию из справочника"""

    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""

    full_name = input("Введите ФИО: ")
    number = input("Введите номер телефона: ")

    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f"\n{full_name.title()} | {number}")


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""

    book = book.split('\n')
    return [contact for contact in book if info.lower() in contact.lower()]


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    
    with open('book.txt', 'r', encoding='utf-8') as file:
            data = file.read()

    user_request = input("Чей номер хочешь найти? Напиши имя: ")
    result = search(data, user_request.lower())

    print(result)


def delete_data():
    '''Удаляет номер по указанной строке'''

    user_number = int(input("Какой номер из справочника хочешь удалить?: "))

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    data = enumerate(data, 1)
    data = filter(lambda x: x[0] != user_number, data)
    data = list(map(lambda x: x[1], data))
    data = "".join(data)

    with open('book.txt', 'w', encoding='utf=8') as file:
        file.write(data)


def change_data():
    '''Изменяет строку в справочнике'''

    user_number = int(input("Какой номер из справочника хочешь поменять?: "))

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    data = data.split('\n')
    data[user_number - 1] = input("\nВведи новую информацию: ")
    data = "\n".join(data)

    with open('book.txt', 'w', encoding='utf=8') as file:
        file.write(data)

