#!/bin/bash
# Update Script for InstaIDUEn5 v2.1-Stable
# Script created by @Sunnam01ram


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is Not installed ... Unable to Update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mUpdating \e[1;94mInstIDU5\e[1;92m ...\n\n"
sleep 1.5
cd ..
rm -rf InstaUser5
git clone https://github.com/sunnamsriram1/InstaUser5.git
cd InstaUser5
chmod +x InstaUserD.sh
printf "\n\e[1;92mRestarting ...\n\e[0m"
bash InstaUserD.sh
cd ..

}

dependencies
script
