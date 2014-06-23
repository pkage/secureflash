#! /bin/sh
cd "$(dirname "$0")"
set -e
openssl aes-256-cbc -d -a -in secure.tgz.enc -out secure.tgz
tar -zxvf secure.tgz
rm secure.tgz
mv secure.tgz.enc .last.tgz.enc
echo "\npress any key to continue"
read -s -n 1
