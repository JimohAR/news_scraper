from datetime import timedelta
from datetime import datetime as dt

import sqlite3
from sqlite3 import Error
from fastapi import FastAPI

from queries import get_news
from news_scraper.settings import SQLITE_URI

app = FastAPI()


@app.get("/")
def read_root():
    return {"App": "Up and Running"}


@app.get("/news")
def read_item(days_back: int = 1) -> dict:
    end_date = make_end_date(days_back)

    news_list = []
    try:
        connection = sqlite3.connect(SQLITE_URI)
        cursor = connection.cursor()
        news_list = cursor.execute(get_news, [end_date]).fetchall()
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        connection.close()

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
