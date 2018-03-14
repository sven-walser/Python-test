#!/usr/bin/env python3

from copy import deepcopy
import gitcd

lst1 = ["a","b",["ab","ba"]]
lst2 = deepcopy(lst1)
lst2[2][1] = "d"
lst2[0] = "c"
print(lst1)
print(lst2)
#zuhause dann cpy und gitcd herunterladen

