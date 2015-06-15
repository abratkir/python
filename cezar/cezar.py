# -*- coding: utf-8 -*-
import sys

def main():
		
	tekst = list(raw_input('Wiadomość do zaszyfrowania: '))
	alfabet = list('abcdefghijklmnopqrstuvwxyz')
	k = int(raw_input('Przesunięcie: '))
	cezar = ''
		
	k = k % 26;	
	
	for c in tekst:
		if c in alfabet:
			cezar += alfabet[(alfabet.index(c)+k)%(len(alfabet))]
		else:
			cezar += ' '
		
	print 'Zaszyfrowana wiadomość: ' + cezar
	

if __name__ == "__main__":
	main()

