#!/usr/bin/env bash

echo "Início coleta mensal..."

cd "coleta/"

#mkdir "all/"	#create all directory
cd "all/"

#create month-year directories (named after the start-month and start-year)
#mkdir "2-2018/" #feito
#mkdir "3-2018/" #nem tudo feito 
#mkdir "4-2018/"
#mkdir "5-2018/"
#mkdir "6-2018/"
#mkdir "7-2018/"
#mkdir "8-2018/"
#mkdir "9-2018/"
#mkdir "10-2018/"
#mkdir "11-2018/"
#mkdir "12-2018/"
#mkdir "1-2019/"

cd .. #leave all

cd .. #leave coleta

echo "directories were created"

#call maker.sh for every month so it will call coleta-tweets.sh for every tag
	#maker call -> ./maker.sh {start_year} {start_month} {end_year} {end_month} {end_day}
	#it always starts on the 16th

#feb 2018
# echo "collecting february ..."
# ./maker.sh "2018" "2" "2018" "3" "16"
# echo "collected february "

#march 2018
#echo "collecting march ..."
#./maker.sh "2018" "3" "2018" "4" "16"
#echo "collected march "

# april 2018
#echo "collecting april ..."
#./maker.sh "2018" "4" "2018" "5" "16"
#echo "collected april "

# may 2018
echo "collecting may ..."
./maker2.sh "2018" "5" "2018" "6" "16"
echo "collected may "

# june 2018
echo "collecting june ..."
./maker.sh "2018" "6" "2018" "7" "16"
echo "collected june "

# july 2018
echo "collecting july ..."
./maker.sh "2018" "7" "2018" "8" "16"
echo "collected july "

# august 2018
echo "collecting august ..."
./maker.sh "2018" "8" "2018" "9" "16"
echo "collected august "

# september 2018
echo "collecting semptember ..."
./maker.sh "2018" "9" "2018" "10" "16"
echo "collected semptember "

# october 2018
echo "collecting october ..."
./maker.sh "2018" "10" "2018" "11" "16"
echo "collected october "

# november 2018
echo "collecting november ..."
./maker.sh "2018" "11" "2018" "12" "16"
echo "collected november "

#december 2018
echo "collecting december ..."
./maker.sh "2018" "12" "2019" "1" "16"
echo "collected december "

#jan 2019
echo "collecting january ..."
./maker.sh "2019" "1" "2019" "2" "17"
echo "collected january "
