create_news_table = """
CREATE TABLE IF NOT EXISTS news (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  link TEXT NOT NULL,
  preview TEXT,
  date_posted TEXT NOT NULL CHECK (date_posted IS DATE(date_posted)),
  photo_link TEXT,
  outlet TEXT NOT NULL
);
"""

insert_news = """
INSERT INTO
  news (title, link, preview, date_posted, photo_link, outlet)
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

get_news = """
SELECT title, link, preview, date_posted, photo_link, outlet
FROM news
WHERE DATE(date_posted) >= DATE(?)
"""
