#!/usr/bin/env python3

from copy import deepcopy

lst1 = ["a","b",["ba","ab"]]

lst2 = deepcopy(lst1)

lst2[2][1] = "d"
lst2[0] = "c"

print(lst1)
print(lst2)

# bei deepcopy wir es wirklich kopiert und bei[:] zeigen einfach nur beide lst auf das gleiche ergebnis

