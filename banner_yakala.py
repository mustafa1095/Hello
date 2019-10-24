#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet -y")
os.system("apt-get install nc -y")
os.system("apt-get install nmap -y")
os.system("clear")
os.system("figlet BANNER YAKALA")
print("""
Bu Araçla Servislerin İlk Açılış(Hoş Geldiniz) Ekranındaki Bilgileri Yakalamak İçin Kullanılır.

1) Tek Servis Banner
2) Tüm Servis Banner

""")

secim = raw_input("Seçim : ")

if(secim=="1"):
	ip = raw_input("Hedef IP : ")
	port = raw_input("Hedef Port : ")
	os.system("clear")
	os.system("figlet BANNER")
	print("")	
	os.system("nc " + ip + " " + port)

if(secim=="2"):
	ip = raw_input("Hedef IP : ")
	os.system("clear")
	os.system("figlet BANNER")
	print("")
	os.system("nmap -sV --script=banner " + ip)
