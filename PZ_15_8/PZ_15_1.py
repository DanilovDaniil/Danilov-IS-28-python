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
    cur.execute("INSERT INTO users VALUES (01, 'Товар 1', 'Заказчик1', '2022-04-15', 2, 10000)")
    cur.execute("INSERT INTO users VALUES (02, 'Товар 2', 'Заказчик2', '2022-05-16', 10, 15000)")
    cur.execute("INSERT INTO users VALUES (03, 'Товар 3', 'Заказчик1', '2022-06-17', 3, 20000)")
    cur.execute("INSERT INTO users VALUES (04, 'Товар 4', 'Заказчик4', '2021-07-18', 10, 25000)")
    cur.execute("INSERT INTO users VALUES (05, 'Товар 5', 'Заказчик1', '2022-04-05', 2, 10000)")
    cur.execute("INSERT INTO users VALUES (06, 'Товар 6', 'Заказчик5', '2024-05-16', 5, 15000)")
    cur.execute("INSERT INTO users VALUES (07, 'Товар 7', 'Заказчик1', '2022-09-07', 5, 40000)")
    cur.execute("INSERT INTO users VALUES (08, 'Товар 8', 'Заказчик3', '2022-07-18', 6, 75000)")
    cur.execute("INSERT INTO users VALUES (09, 'Товар 9', 'Заказчик1', '2022-08-27', 3, 7000)")
    cur.execute("INSERT INTO users VALUES (10, 'Товар 10', 'Заказчик5', '2023-07-18', 9, 300000)")
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)

