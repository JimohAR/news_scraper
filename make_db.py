import sqlite3
from sqlite3 import Error

from news_scraper.settings import SQLITE_URI
from queries import create_news_table


if __name__ == "__main__":
    try:
        connection = sqlite3.connect(SQLITE_URI)
        cursor = connection.cursor()
        cursor.execute(create_news_table)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        connection.close()
