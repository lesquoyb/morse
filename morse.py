#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Lesquoy Baptiste 05/07/2014
import pyglet
import time
import sys

def read(char):
    for c in char:
        music="sounds/longBeep.wav" if (c=="-")  else "sounds/shortBeep.wav"
        sound = pyglet.resource.media(music)
        sound.play()
        time.sleep(0.6)
    time.sleep(0.9)

def wrap(text):
	print(text)

if __name__ == '__main__':
    corresp={'4': '····-', 'S': '···', 'G': '--·', 'H': '····', 'A': '·-', 'O': '---', '6': '-····', 'Q': '--·-', '/': '-··-·', '8': '---··', 'W': '·--', '$': '···-··-', ';': '-·-·-·', 'B': '-···', '0': '-----', 'P': '·--·', '&': '·-···', ')': '-·--·-', 'U': '··-', 'C': '-·-·', '.': '·-·-·-', '5': '·····', 'K': '-·-', 'D': '-··', 'ç': '-·-··', 'F': '··-·', '+': '·-·-·', 'I': '··', 'R': '·-·', ':': '---···', 'é': '··-··', 'à': '·--·-', '"': '·-··-·', 'V': '···-', 'J': '·---', '3': '···--', 'ö': '---·', '(': '-·--·', '9': '----·', 'T': '-', 'è': '·-··-', "'": '·----·', 'L': '·-··', '@': '·--·-·', 'N': '-·', '!': '-·-·--', ',': '--··--', '7': '--···', '1': '·----', 'ü': '..--', '?': '..--..', '=': '-···-', 'M': '--', 'X': '-··-', 'E': '·', 'Y': '-·--', '_': '··--·-', 'Z': '--··', '2': '··---', '-': '-····-'}
    print (sys.argv)
    fun = read if ( len(sys.argv) == 1 ) else ( wrap if (sys.argv[1]=="text") else None)
    if(fun != None):
        phrase=raw_input("entrez la phrase à transformer en morse\n")
        for c in phrase.replace(" ",""):
            fun(corresp[c.upper()])
    else:
        print("les paramètres ne sont pas bon: vous pouvez soit ne pas en mettre pour transformer la phrase en son soit mettre 'text' pour la transformer en texte")  
