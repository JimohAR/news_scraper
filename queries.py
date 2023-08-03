create_news_table = """
CREATE TABLE IF NOT EXISTS news (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  link TEXT NOT NULL,
  preview TEXT,
  date TEXT,
  photo_link TEXT,
  outlet TEXT NOT NULL
);
"""

insert_news = """
INSERT INTO
  news (title, link, preview, date, photo_link, outlet)
VALUES
  (?, ?, ?, ?, ?, ?);
"""

remove_duplicates = """
DELETE FROM news
WHERE rowid NOT IN (
  SELECT MIN(rowid) 
  FROM news 
  GROUP BY link
)
"""
