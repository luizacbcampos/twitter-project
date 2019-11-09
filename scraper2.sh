#!/usr/bin/env bash
year=($1) 
month=($2)

end_y=($3)
end_m=($4)
end_d=($5)

#28
#./coleta-tweets.sh "coleta" "guns" "gun OR guns" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "guns"


# PASTAS E ETC

limite="${month}""-""${year}"
echo "${limite}"


cd "coleta/"
mv "guns/" "all/"

cd "all/"

mv "guns/" "${limite}"

cd ../..

