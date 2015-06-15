import sys 

def encrypt(k):
	plaintext = raw_input('Wprowadzona wiadomosc do zaszyfrowania: ')
	wiadomosc = ''
	
	for each in plaintext:
		c = (ord(each)+k) % 26
		
		if c < 32: 
			c+=31
			
		wiadomosc += chr(c)
		
	print 'Zaszyfrowana wiadomosc: ' + wiadomosc

def decrypt(k):
	wiadomosc = raw_input('Wprowadzona zaszyfrowana wiadomosc: ')
	plaintext = ''
	
	for each in wiadomosc:
		p = (ord(each)-k) % 126
	
		if p < 32:
			p+=95
						
		plaintext += chr(p)
		
	print 'Odszyfrowana wiadomosc: ' + plaintext

def main(argv):
	if (len(sys.argv) != 3):
		sys.exit('Podano za malo argumentow wywolania programu. [nazwaPliku oIlePrzesunac s/o] (s - szyfrowania, o - odszyfrowanie)')
		
	if sys.argv[2] == 's':
		encrypt(int(sys.argv[1]))
	elif sys.argv[2] == 'o':
		decrypt(int(sys.argv[1]))
	else:
		sys.exit('Zle podany tryb pracy. Tylko s lub o.')


if __name__ == "__main__":
	main(sys.argv[1:])

