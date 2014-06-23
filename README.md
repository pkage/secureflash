secureflash
===========

a simple tool to tarball and encrypt a folder

---

###usage

- run ```mount.command``` to decrypt and decompress the folder
- run ```unmount.command``` to compress and encrypt the folder

---

###notes

- don't remove or rename ```secure/```
- when you decompress, the encrypted file is renamed to ```.last.tgz.enc```, so if you need to recover the file you'll be able to.
