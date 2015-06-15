import sys, math,string
import linecache
from Crypto.Cipher import ARC4

def entropia(dane):
	prawd = [ float(dane.count(c)) / len(dane) for c in dict.fromkeys(list(dane)) ]
	wynik = - sum([ p * math.log(p) / math.log(2.0) for p in prawd ])
	return wynik
pomoc = 10.0
klucz = ''

if __name__ == '__main__':
	plik = open('zaszyfrowane.txt').readlines()
	wiersz = linecache.getline('zaszyfrowane.txt', 1)
	chars = string.ascii_letters
	for a in chars:
		for b in chars:
			for c in chars:
				pom = a+b+c
				cipher = ARC4.new(pom)
				enc2 = cipher.encrypt(wiersz)
				enc2 = entropia(enc2)
				if pomoc > enc2:
					pomoc = enc2
					klucz = pom
	print klucz
	cipher = ARC4.new(klucz)
	odszyfrowane = cipher.encrypt(wiersz)
	print odszyfrowane[:len(odszyfrowane)-1]
