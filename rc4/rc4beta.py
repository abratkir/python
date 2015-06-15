
#
def RC4 (key):
	S = rejestr(key)
	return strumien(S)

# Inicjalizowanie rejestru:
def rejestr (key):
	S = range(256)
	i = 0
	for i in range(256):
		S[i] = i
	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % len(key)]) % 256
		S[i], S[j] = S[j], S[i]
	return S
    

# Generowanie strumienia klucza
def strumien (st):
	i = 0
	j = 0
	while True:
		i = (i + 1) % 256
		j = (j + st[i]) % 256
		st[i], st[j] = st[j], st[i]
		K = st[(st[i] + st[j]) % 256]
		yield K

	
    
if __name__ == "__main__":
	
	#BBF316E8D940AF0AD3
    klucz = 'klu'
    #tekst = "Plaintext"

    #1021BF0420
    #klucz = 'Wiki'
    #tekst = 'pedia'

    #45A01F645FC35B383552544B9BF5
    #klucz = 'Secret'
    #tekst = 'Attack at dawn'

    def convert_key(s):
        return [ord(c) for c in s]
        
        
    szyfrowane = ''
        
    import sys
    tekst = list(raw_input('Wiadomosc do zaszyfrowania: '))
	#klucz = list(raw_input('Wprowadz klucz: '))
    klucz = convert_key(klucz)

    strumienKluczy = RC4(klucz)

	
    
    for c in tekst:
		help = chr(ord(c) ^ strumienKluczy.next())
		szyfrowane = szyfrowane + help
    sys.stdout.write("%s" % szyfrowane)
    plik = open('zaszyfrowane.txt', 'w')
    plik.write(szyfrowane)
    plik.close()
