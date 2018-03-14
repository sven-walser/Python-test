#!/usr/bin/env python3


lst1 = ["a","b",["ab","ba"]]
lst2 = lst1[:]
lst2[0] = "c"
lst2[2][1] = "d"

print(lst1)

print(lst2)
#Man erkennt, dass man aber nicht nur die Einträge in lst2 geändert hat, sondern auch den Eintrag von lst1[2][1]. 
#Dies liegt daran, dass in beiden Listen, also lst1 und lst2, das jeweils dritte Element nur ein Link auf eine physikalisch gleiche Unterliste ist. Diese Unterliste wurde nicht mit [:] mitkopiert. 

