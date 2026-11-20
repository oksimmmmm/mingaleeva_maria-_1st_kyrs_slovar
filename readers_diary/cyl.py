book = []

def add_book():
    name_book = input("введите название книги:").strip()
    if not name_book:
        print("здесь нечего нету еще")
        return
    if name_book in book:
        print("такая книга уже есть")
        return
    if not name_book:
        print("название пустое")
        return
    book.append(name_book)
def show_all_book():
    if not book:
        print("здесь нечего нету еще")
        return
    for i in range(len(book)):
        print(f"{i + 1},{book[i]}")
def show_five_book():
    if not book:
        print("здесь нечего нету еще")
        return
    last_num = book[-5]
    start_num = len(last_num) - len(last_num) + 1
    for i in range(len(last_num)):
        books = last_num[i]
        real_num = start_num + 1
        print(f"{real_num}, {books}")
def set_new():
    if not book:
        print("здесь нечего нету еще")
        return
    new_name = input("введите новое название книги:").strip()
    index_name = input("введите номер для замены:").strip()
    if not index_name.isdigit():
        print("номер должен быть числом!")
        return
    index = int(index_name)
    if not (1 <= index <= len(book)) or not new_name:
        print("ошибка")
        return
    book[num - 1] = new_name
    print("вы поменяли название")

def faind_book():
    if not book:
        print("здесь нечего нету еще")
        return
    scherh_name = input("введите название:").strip().lower()
    found = False
    for i in range(len(book)):
        if scherh_name in book[i].lower():
            print(f"{i + 1},{book[i]} эта книга есть в списке")
            found = True
    if not found:
        print("нечего не найдено")
def statik():
    if not book:
        print("здесь нечего нету еще")
        return
    print(f"всего :{len(book)}, первая книга: {book[0]}, последняя книга: {book[-1]}")
while True:
    
    print("===  ЧИТАТЕЛЬСИЙ ДНЕВНИК ===")
    print("1 -  добавить книгу\n2 - показать все книги\n3 - Показать посление 5 книг\n4 - Заменить название по номеру\n5 - Поиск по названию\n6 - Статистика\n0 - Выход")
    try:
        num = int(input())
    except ValueError:
        print("что то введено не так")
        continue
    if num == 0:
        print("программа закончена")
        break
    elif num == 1:
        add_book()
    elif num == 2:
        show_all_book()
    elif num == 3:
        show_five_book()
    elif num == 4:
        set_new()
    elif num == 5:
        faind_book()
    elif num == 6:
        statik()
