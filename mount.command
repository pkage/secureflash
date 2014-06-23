#! /bin/sh
cd "$(dirname "$0")"
set -e
tar -cvvf secure.tgz secure/
openssl aes-256-cbc -a -salt -in secure.tgz -out secure.tgz.enc
rm secure.tgz
if [ -e secure.tgz.enc -a -f secure.tgz.enc ]
then
	rm -rf secure
	echo "operation complete."
else
	echo "operation appears to have failed."
fi  


echo "press any key to exit"
read -s -n 1
