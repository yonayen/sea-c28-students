#!/usr/bin/env python


import string

rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

string.translate("Yonathan Ayenew!", rot13)

if __name__ == '__main__':