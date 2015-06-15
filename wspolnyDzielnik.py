import sys
import string

def nwd ( a , b ):
	while b!=0:
		temp = a % b
		a = b
		b = temp
	return a


def nww ( a , b):
	return a*b/nwd(a,b)


firstNumber =  int(sys.argv[1])
secondNumber =  int(sys.argv[2])
if nww(firstNumber , secondNumber) == firstNumber * secondNumber:
	print "Liczby sa wzglednie pierwsze"
else:
	print "Liczby nie sa wzglednie pierwsze"

