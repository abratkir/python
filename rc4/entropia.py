import sys, re, string, fileinput, math

plik=open('zaszyfrowane.txt')
ileZnakow=0;
ileRoznych=0;

stat = {}

line = list(raw_input('Tekst: '))
for znak in line:
	ileZnakow += 1
	if znak in stat:
		stat[znak] += 1
	else:
		stat[znak] = 0
		ileRoznych += 1

entropia=0;
for znak in stat:
	p=(float(stat[znak]+1)/float(ileZnakow))
	entropia += - (p * math.log(p, 2))

print "entropia: ", entropia




