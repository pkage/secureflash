#! /usr/bin/env python

import os

print "setting up encryption..."
mnt = open("mount.command", 'w')
mnt.write("""#! /bin/sh
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
read -s -n 1""")
mnt.close()


unmnt = open("unmount.command". 'w')
unmnt.write("""#! /bin/sh
cd "$(dirname "$0")"
set -e
openssl aes-256-cbc -d -a -in secure.tgz.enc -out secure.tgz
tar -zxvf secure.tgz
rm secure.tgz
mv secure.tgz.enc .last.tgz.enc
echo "\npress any key to continue"
read -s -n 1""")
unmnt.close()


os.mkdir("secure")
