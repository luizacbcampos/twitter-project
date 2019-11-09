#!/usr/bin/env bash

TYPE=$1 #string
LABEL=$2 # string
keyword=$3 #string
year=($4) 
month=($5)

end_y=($6)
end_m=($7)
end_d=($8)
# updates
mkdir -p "${TYPE}/${LABEL}/"
cp -R TweetScraper/scrapy.cfg "${TYPE}/${LABEL}/"scrapy.cfg
cp -R TweetScraper/TweetScraper "${TYPE}/${LABEL}/"TweetScraper
cd "${TYPE}/${LABEL}/"
mkdir -p "scrapy-log/"

time_range=" since:"${year}"-"${month}"-16 until:"${end_y}"-"${end_m}"-"${end_d}

start=$SECONDS
echo "${time_range}"
echo "scraping ${keyword}${time_range} -a lang=en -a top_tweet=False ... "
scrapy crawl TweetScraper -a query="${keyword}${time_range}" -a lang="en" &> "scrapy-log/${LABEL}-${month}-${year}".log

duration=$(( SECONDS - start))

echo "scraped ${keyword}${time_range} ... time elapsed: "$duration" seconds"

