#/bin/bash

## USAGE
function display_usage() { 
	echo "This script must be run with super-user privileges." 
	echo -e "\nUsage: $0 'bot_token' \n" 
	} 
# if less than 1 arguments supplied, display usage 
	if [  $# -le 0 ] 
	then 
		display_usage
		exit 1
	fi 
 
# check whether user had supplied -h or --help . If yes display usage 
	if [[ ( $# == "--help") ||  $# == "-h" ]] 
	then 
		display_usage
		exit 0
	fi 
 
# display usage if the script is not run as root user 
	if [[ "$EUID" -ne 0 ]]; then 
		echo "This script must be run as root!" 
		exit 1
	fi 

TOKEN = $1

apt-get install git -y
pip3 install python-telegram-bot nanpy --upgrade

git clone "https://github.com/hyerakon/sippy-controller.git" /opt

echo "$TOKEN---" > "/opt/sippy-controller/tokens.txt"
python3 /opt/sippy-controller/sippy_controller_bot.py

exit 0


