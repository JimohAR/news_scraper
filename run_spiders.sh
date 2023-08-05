# run inside active project ./
# . .venv/bin/activate
python make_db.py

scrapy crawl punch -O data/punch.json -a days=1
scrapy crawl leadership -O data/leadership.json -a days=1
scrapy crawl dailypost -O data/dailypost.json -a days=1
