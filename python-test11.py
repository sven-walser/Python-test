#!/usr/bin/env python3

from time import sleep

i = 1

while True:
	i = i + 1
	
	if i % 3:
		continue
	
	print(i)
	sleep(2)

# modulo (% 3) gibt nur sachen an die durch 3 teilbar sind
