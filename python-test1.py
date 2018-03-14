#!/usr/bin/env python3

lst1 = ["a","b",["ab","ba"]]
lst2 = lst1[:]
lst2[2][1] = "d"
print(lst2)
print(lst1)
#wenn man bei lst[2] etwaws überschreibt ersetzt es die gesame zwischenliste. Wenn man aber schreibt liste[2][1] ersetzt es nur das zweite element in der zwischenliste

