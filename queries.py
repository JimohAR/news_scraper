create_news_table = """
CREATE TABLE IF NOT EXISTS news (
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  link TEXT NOT NULL,
  preview TEXT,
  date_posted DATE NOT NULL,
  photo_link TEXT,
  outlet TEXT NOT NULL
);
"""

insert_news = """
INSERT INTO
  news (title, link, preview, date_posted, photo_link, outlet)
VALUES
  (%s, %s, %s, %s, %s, %s);
"""

remove_duplicates = """
DELETE FROM news a USING (
    SELECT MIN(ctid) as ctid, link
    FROM news 
    GROUP BY link HAVING COUNT(*) > 1
) b
WHERE a.link = b.link 
AND a.ctid <> b.ctid
"""

get_news = """
SELECT title, link, preview, date_posted, photo_link, outlet
FROM news
WHERE date_posted >= %s::DATE
"""
