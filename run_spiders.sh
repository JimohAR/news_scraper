# run inside active project ./
. .venv/bin/activate
scrapy crawl punch -O data/punch.json
scrapy crawl leadership -O data/leadership.json
scrapy crawl dailypost -O data/dailypost.json
