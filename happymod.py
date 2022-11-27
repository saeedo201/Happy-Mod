#!/usr/bin/python

import os, sys, time

##colorize##
w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33m"
d="\033[2;31m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"
W="\033[47m"
R="\033[41m"
B="\033[30m"
G="\033[90m"
BG="\033[100m"

print(p+"[*]"+w+" prepeare for installing all dependencies")
print(g+"[+]"+w+" colud take a while please wait")
os.system("cd $HOME")

Zipalign = os.system("command -v zipalign &> /dev/null")
if Zipalign == 0:
	print(g+"[✓]"+w+" zipalign is already exists")
else:
	print(R+"[!]"+w+" zipalign is not found")
	os.system("pkg install -y zipalign &> /dev/null")
Apktool = os.system("command -v apktool &> /dev/null")
if Apktool == 0:
	print(g+"[✓]"+w+" apktool is already exists")
else:
	print(R+"[!]"+w+" installing apktool")
	print(p+"[+] this could take a while please wait")
	os.system("pkg install -y apktool &> /dev/null")
Proot = os.system("command -v proot &> /dev/null")
if Proot == 0:
	print(g+"[✓]"+w+" proot is already exists")
else:
	print(p+"[*]"+w+" installing proot ")
	os.system("pkg install -y proot wget &> /dev/null")
Java = os.system("command -v java &> /dev/null")
if Java == 0:
	print(g+"[✓]"+w+" java is already exists")
else:
	print(p+"[*]"+w+" installing java")
	os.system("wget https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava &> /dev/null")
Aapt = os.system("command -v aapt &> /dev/null")
if Aapt == 0:
	print(g+"[✓]"+w+" aapt is already exists")
else:
	print(p+"[*]"+w+" installing aapt")
	os.system("pkg install -y aapt &> /dev/null")
Apksigner = os.system("command -v apksigner &> /dev/null")
if Apksigner == 0:
	print(g+"[✓]"+w+" apksigner is already exists")
else:
	print(p+"[*]"+w+" installing apksigner")
	os.system("pkg install -y apksigner &> /dev/null")
Metasploit = os.system("command -v msfconsole &> /dev/null")
if Metasploit == 0:
	print(g+"[✓]"+w+" metasploit is already exists")
else:
	print(p+"[*]"+w+" installing metasploit-framework")
	os.system("pkg install -y openssl &> /dev/null")
	os.system("pkg install -y openssh &> /dev/null")
	os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod 777 metasploit.sh && bash metasploit.sh &> /dev/null")
print(g+"[✓]"+w+" all packges has been installed")
