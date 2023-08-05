from datetime import timedelta
from datetime import datetime as dt

from fastapi import FastAPI

import psycopg2
from psycopg2 import OperationalError as Error

from queries import get_news
from news_scraper.settings import POSTGRESQL_URI

app = FastAPI()


@app.get("/", tags=["ROOT"])
def read_root():
    return {"App": "Up and Running"}


@app.get("/news", tags=["NEWS"])
def read_item(days_back: int = 1) -> dict:
    end_date = make_end_date(days_back)

    news_list = []
    try:
        connection = psycopg2.connect(POSTGRESQL_URI)
    except Error as e:
        print(f"The error '{e}' occurred")
        return {}

    cursor = connection.cursor()
    cursor.execute(get_news, [end_date])
    news_list = cursor.fetchall()

    new_l = []
    for news in news_list:
        new_l.append(
            dict(zip(("title", "link", "preview", "date", "photo_link", "outlet"), news))
        )

    return {
        "news": new_l
    }


def make_end_date(days_back: int) -> str:
    end_date = dt.today() - timedelta(days=days_back)

    return end_date.date().isoformat()
