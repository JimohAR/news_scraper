import psycopg2
from psycopg2 import OperationalError as Error

from news_scraper.settings import POSTGRESQL_URI
from queries import create_news_table


if __name__ == "__main__":
    try:
        connection = psycopg2.connect(POSTGRESQL_URI)
    except Error as e:
        print(f"The error '{e}' occurred")
        exit()

    cursor = connection.cursor()
    cursor.execute(create_news_table)
    connection.commit()
