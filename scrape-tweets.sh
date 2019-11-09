#!/usr/bin/env bash

TYPE=$1 #string
LABEL=$2 # string
keyword=$3 #string
years=($4) #(2014 2015 2016 2017 2018 2019)
months=($5) #(1 2 3 4 5 6 7 8 9 10 11 12)
m_days=(31 28 31 30 31 30 31 31 30 31 30 31)
local="\"United States\""
near=" near:"
within=" within:2000mi"
years_leap=(2000 2004 2008 2012 2016 2020 2024 2028 2032 2036 2040 2044 2048)
year_stop=2019
month_stop=10

# updates
mkdir -p "${TYPE}/${LABEL}/"
cp -R TweetScraper/scrapy.cfg "${TYPE}/${LABEL}/"scrapy.cfg
cp -R TweetScraper/TweetScraper "${TYPE}/${LABEL}/"TweetScraper
cd "${TYPE}/${LABEL}/"
mkdir -p "scrapy-log/"

# loop
for i in "${years[@]}"
do
   if [[ " ${years_leap[@]} " =~ " ${i} " ]]; then
       last_day=29
   else
       last_day=28
   fi

   for j in "${months[@]}"
   do
       if [[ ${j} == 2 ]]; then
           if [[ ${m_days[$(( j - 1 ))]} -ge ${last_day} ]]; then
             time_range=" since:"$i"-"${j}"-1 until:"$i"-"${j}"-"${last_day}
           else
             time_range=" since:"$i"-"${j}"-1 until:"$i"-"${j}"-"${m_days[$(( j - 1 ))]}
           fi
       else
           time_range=" since:"$i"-"${j}"-1 until:"$i"-"${j}"-"${m_days[$(( j - 1 )) ]}
       fi

       if [[ $i -ge $year_stop ]]; then
           if [[ $j -ge $month_stop ]]; then
               break
           fi
       fi

       start=$SECONDS
        #editei
       time_range=" since:2018-02-16 until:2018-05-16"
       #fim editei
       echo "scraping ${keyword}${time_range} -a lang=en -a top_tweet=True... "
       #near=${near}${local}${within}
       #echo "${keyword}${near}${time_range}"
       scrapy crawl TweetScraper -a query="${keyword}${time_range}" -a lang="en" -a top_tweet="True" &> "scrapy-log/${LABEL}-${i}-${j}".log
       duration=$(( SECONDS - start))

       echo "scraped ${keyword}${time_range} ... time elapsed: "$duration" seconds"
   done
done

cd ..
