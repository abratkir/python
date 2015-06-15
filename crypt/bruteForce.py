# -*- coding: utf-8 -*-
import sys, string, crypt

tekst = open('passwd.txt').read()
passwd = ''

for x in tekst:
	if x != '\n':
		passwd += str(x)
	if x == ':':
		passwd = ''
		
chars = string.ascii_letters
trial=''

for a in chars:
	for b in chars:
		for c in chars:
			trial = a+b+c
			crypted = crypt.crypt( trial, passwd)
			if crypted == passwd:
				print "Hasło złamane: %s" % (a+b+c)
				break
		if crypted == passwd:
			break
	if crypted == passwd:
		break
		
if crypted != passwd:
	print "Hasło niezłamane"
