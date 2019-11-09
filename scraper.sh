#!/usr/bin/env bash
year=($1) 
month=($2)

end_y=($3)
end_m=($4)
end_d=($5)

#1
./coleta-tweets.sh "coleta" "2nd" "\"2nd amendment\""  "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "2nd"

#2
./coleta-tweets.sh "coleta" "gunsense" "# gunsense" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "gunsense"

#3
./coleta-tweets.sh "coleta" "MarchForOurLives" "# MarchForOurLives" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "MarchForOurLives"

#4
./coleta-tweets.sh "coleta" "NeverAgain" "# NeverAgain" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "NeverAgain"

#5
./coleta-tweets.sh "coleta" "gunrights" "# gunrights" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "gunrights"

#6
./coleta-tweets.sh "coleta" "protect2a" "# protect2a" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "protect2a"

#7
./coleta-tweets.sh "coleta" "molonlabe" "# molonlabe" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "molonlabe"

#8
./coleta-tweets.sh "coleta" "molonlab" "# molonlab" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "molonlab"

#9
./coleta-tweets.sh "coleta" "noguncontrol" "# noguncontrol" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "noguncontrol"

#10
./coleta-tweets.sh "coleta" "progun" "# progun"  "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "progun"

#11 
./coleta-tweets.sh "coleta" "nogunregistry" "# nogunregistry" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "nogunregistry"

#12 
./coleta-tweets.sh "coleta" "votegunrights" "# votegunrights" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "votegunrights"

#13 
./coleta-tweets.sh "coleta" "firearmrights" "# firearmrights" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "firearmrights"

#14 
./coleta-tweets.sh "coleta" "gungrab" "# gungrab" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "gungrab"

#15
./coleta-tweets.sh "coleta" "gunfriendly" "# gunfriendly" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "gunfriendly"

#16
./coleta-tweets.sh "coleta" "gunviolence" "# gunviolence"  "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "gunviolence"

#17
./coleta-tweets.sh "coleta" "gunsensepatriot" "# gunsensepatriot" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "gunsensepatriot"

#18
./coleta-tweets.sh "coleta" "votegunsense" "# votegunsense" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "votegunsense"

#19
./coleta-tweets.sh "coleta" "guncontrolnow" "# guncontrolnow" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "guncontrolnow"

#20
./coleta-tweets.sh "coleta" "momsdemandaction" "# momsdemandaction" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "momsdemandaction"

#21
./coleta-tweets.sh "coleta" "momsdemand" "# momsdemand" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "momsdemand"

#22
./coleta-tweets.sh "coleta" "demandaplan" "# demandaplan" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "demandaplan"

#23
./coleta-tweets.sh "coleta" "nowaynra" "# nowaynra" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "nowaynra"

#24
./coleta-tweets.sh "coleta" "gunskillpeople" "# gunskillpeople" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "gunskillpeople"

#25
./coleta-tweets.sh "coleta" "endgunviolence" "# endgunviolence" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "endgunviolence"

#26- al
./coleta-tweets.sh "coleta" "second_am" "\"second amendment\"" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "second_am"

#27 -al
./coleta-tweets.sh "coleta" "firearms" "firearm OR firearms" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "firearms"

#28
./coleta-tweets.sh "coleta" "guns" "gun OR guns" "${year}" "${month}" "${end_y}" "${end_m}" "${end_d}"
./MAIN-consolidater.sh "coleta" "guns"


# PASTAS E ETC

limite="${month}""-""${year}"
echo "${limite}"


cd "coleta/"
#mkdir  "all/${limite}"
mv "2nd/" "all/"
mv "gunsense/" "all/"
mv "MarchForOurLives/" "all/"
mv "NeverAgain/" "all/"
mv "gunrights/" "all/"
mv "protect2a/" "all/"
mv "molonlabe/" "all/"
mv "molonlab/" "all/"
mv "noguncontrol/" "all/"
mv "progun/" "all/"
mv "nogunregistry/" "all/"
mv "votegunrights/" "all/"
mv "firearmrights/" "all/"
mv "gungrab/" "all/"
mv "gunfriendly/" "all/"
mv "gunviolence/" "all/"
mv "gunsensepatriot/" "all/"
mv "votegunsense/" "all/"
mv "guncontrolnow/" "all/"
mv "momsdemandaction/" "all/"
mv "momsdemand/" "all/"
mv "demandaplan/" "all/"
mv "nowaynra/" "all/"
mv "gunskillpeople/" "all/"
mv "endgunviolence/" "all/"
mv "second_am/" "all/"
mv "firearms/" "all/"
mv "guns/" "all/"

cd "all/"


mv "2nd/" "${limite}"
mv "gunsense/" "${limite}"
mv "MarchForOurLives/" "${limite}"
mv "NeverAgain/" "${limite}"
mv "gunrights/" "${limite}"
mv "protect2a/" "${limite}"
mv "molonlabe/" "${limite}"
mv "molonlab/" "${limite}"
mv "noguncontrol/" "${limite}"
mv "progun/" "${limite}"
mv "nogunregistry/" "${limite}"
mv "votegunrights/" "${limite}"
mv "firearmrights/" "${limite}"
mv "gungrab/" "${limite}"
mv "gunfriendly/" "${limite}"
mv "gunviolence/" "${limite}"
mv "gunsensepatriot/" "${limite}"
mv "votegunsense/" "${limite}"
mv "guncontrolnow/" "${limite}"
mv "momsdemandaction/" "${limite}"
mv "momsdemand/" "${limite}"
mv "demandaplan/" "${limite}"
mv "nowaynra/" "${limite}"
mv "gunskillpeople/" "${limite}"
mv "endgunviolence/" "${limite}"
mv "second_am/" "${limite}"
mv "firearms/" "${limite}"
mv "guns/" "${limite}"

cd ../..

