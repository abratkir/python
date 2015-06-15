# -*- coding: utf-8 -*-
import sys

def main(argv):
	if (len(sys.argv) != 1):
		sys.exit('Podano za mało argumentów podczas wywołania programu.')
		
	tekst = list(raw_input('Wiadomość do odszyfrowania: '))
	alfabet = list('abcdefghijklmnopqrstuvwxyz')
	cezar = ''

	wystapienia = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	
	for c in tekst:
		if c in alfabet:
			wystapienia[alfabet.index(c)] += 1	
	
	indeks = 0
	
	for i in range(26):
		if wystapienia[indeks] < wystapienia[i]:
			indeks = i		
			
	k = -indeks
	for c in tekst:
		if c in alfabet:
			cezar += alfabet[(alfabet.index(c)+k)%(len(alfabet))]
		else:
			cezar += ' '
		
	print 'Zaszyfrowana wiadomosc: ' + cezar

if __name__ == "__main__":
	main(sys.argv[1:])

