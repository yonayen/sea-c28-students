#!/usr/bin/env python


import string

rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

string.translate("Yonathan Ayenew!", rot13)


if __name__ == '__main__':

dictionary = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m'}	

def rot(xy):
	rot13 = ''
	for letter in xy:
		if letter.islower():
			rot13 =+ dictionary.get(letter)
		else:
			print 'now working'

	for letter in xy:
		if letter.isupper():
			letter = letter.lower()
			rot13 =+ dictionary.get(letter).capitalize()
		else:
			print 'not working'

	# This obviously needs a lot of work.  I'll revisit it again. I'm over thinking a simple test.

