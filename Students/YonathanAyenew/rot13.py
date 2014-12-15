#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Compute rot13 -- replace letter with one 13 places further in alphabet"""

dictionary = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s','g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m'}


def rot(word):
    rot = []
    for c in word:
        if c.islower():
            rot.append(dictionary.get(c))
        if c.isupper():
            c = c.lower()
            result = dictionary.get(c)
            rot.append(result.capitalize())
        if c not in dictionary:
            rot.append(c)
 
    return ''.join(rot)



if __name__ == '__main__':

    dictionary = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s', 'g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e', 's':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m'}  
    
    input = "Yonathan Ayenew"
    rot_reverse = "Lbanguna Nlrarj"

    assert rot("Yonathan Ayenew") == rot_reverse
    
    print "Assert test works"
