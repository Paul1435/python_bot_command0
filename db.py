import sqlite3
from datetime import datetime
import deadline

# cursor.execute("CREATE TABLE IF NOT EXISTS event (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR[100], comment VARCHAR[1000], date DATETIME)")
# cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY AUTOINCREMENT, telegramId INTEGER UNIQUE)")

database_path = "tgbot.sql"
conn = sqlite3.connect(database_path)


def insert_user_id_db(user_id: int):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO persons(telegramId) VALUES({user_id})")
    conn.commit()
    cursor.close()


def is_user_id_in_db(user_id: int) -> bool:
    cursor = conn.cursor()
    cursor.execute(f"SELECT EXISTS(SELECT * FROM persons WHERE telegramId = {user_id})")
    return cursor.fetchall()[0][0]


def delete_user_id_db(user_id: int):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM persons WHERE telegramId = {user_id}")
    conn.commit()
    cursor.close()


def insert_deadline(dl: deadline.Deadline):
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO event(name, date, comment)  VALUES ('{dl.name}', '{dl.date.strftime('%Y-%m-%d %H:%M:%S')}', '{dl.comment}')")
    conn.commit()
    cursor.close()


def delete_deadline_id(id_deadline: int):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM event WHERE id = {id_deadline}")
    conn.commit()
    cursor.close()


def delete_deadline_date(date: datetime):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM event WHERE date = '{date.strftime('%Y-%m-%d %H:%M:%S')}'")
    conn.commit()
    cursor.close()


def delete_deadline_date_interval(start_date: datetime, finish_date: datetime):
    cursor = conn.cursor()
    cursor.execute(
        f"DELETE FROM event WHERE date >= '{start_date.strftime('%Y-%m-%d %H:%M:%S')}' AND date <= '{finish_date.strftime('%Y-%m-%d %H:%M:%S')}'")
    conn.commit()
    cursor.close()


def show_all_deadlines() -> list[deadline.Deadline]:
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM event ORDER BY date")
    tuple_deadlines = cursor.fetchall()

    deadlines = []
    for dl in tuple_deadlines:
        cur_deadline = deadline.Deadline(dl[1], dl[2], datetime.strptime(dl[3], "%Y-%m-%d %H:%M:%S"))
        cur_deadline.id = dl[0]
        deadlines.append(cur_deadline)
    cursor.close()
    return deadlines


def show_all_users():
    cursor = conn.cursor()
    cursor.execute(f"SELECT telegramId FROM persons")
    people = cursor.fetchall()
    cursor.close()
    return people
