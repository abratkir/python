import sys

def main(argv):
	if (len(sys.argv) != 1):
		sys.exit('Podano za malo argumentow podczas wywolania programu.')
		
	tekst = list(raw_input('Tekst na podstawie, ktorego wyznaczamy statystyke: '))
	alfabet = list('abcdefghijklmnopqrstuvwxyz')
	cezar = ''

	wystapienia = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	
	for c in tekst:
		if c in alfabet:
			wystapienia[alfabet.index(c)] += 1	
	
		
	for indeks in range(26):
		if wystapienia[indeks] > 0:
			print "%s <=> %d " % (alfabet[indeks], wystapienia[indeks])
			
	k = 0
	for i in range(26):
		if wystapienia[k] < wystapienia[i]:
			k = i		
	
	print "Najczesciej wystepujacy znak:" + alfabet[k]
			
			

if __name__ == "__main__":
	main(sys.argv[1:])

