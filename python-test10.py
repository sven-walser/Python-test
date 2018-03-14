#!/usr/bin/env python3

import sys

text = ""

while 1:
	c = sys.stdin.read(1)
	print("aktuelles Zeichen: %s" % c)
	text = text + c
	if c =="\n":
		break

print("Du hast %s eingegeben" % (text))
print("Du hast ", text, " eingegeben")

#sobald man einen zeilenumbruch (\n) eingiebt wird durch break die schleife unterbrochen
