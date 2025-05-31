# Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказов
# торговой фирмы. Таблица Заказы должна содержать информацию о товарах со
# следующей структурой записи: Код товара, Наименование товара, Заказчик
# (наименование организации, возможны повторяющиеся значения), Дата заказа, Срок
# исполнения (от 1 до 10 дней), Стоимость заказа.

import sqlite3

with sqlite3.connect('Zakazi.db') as con:
    cur = con.cursor()
    cur.execute("drop table if exists users")
    cur.execute("""create table if not exists users (
    id_tov int,
    name text not null,
    zakazchik text not null,
    date_z date not null,
    srok int check (srok between 1 and 10) not null,
    cell decimal(10, 2)
    )""")
    cur.execute("INSERT INTO users VALUES (1, 'Товар 1', 'Заказчик1', '2022-04-15', 2, 10000)")
    cur.execute("INSERT INTO users VALUES (2, 'Товар 2', 'Заказчик2', '2022-05-16', 1, 15000)")
    cur.execute("INSERT INTO users VALUES (3, 'Товар 3', 'Заказчик1', '2022-06-17', 3, 20000)")
    cur.execute("INSERT INTO users VALUES (4, 'Товар 4', 'Заказчик4', '2022-07-18', 10, 25000)")
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)

