#!/usr/bin/env python3
age = int(input("Alter des Hundes: "))


if age < 0:
	print("Das stimmt wohl kaum!")
elif age == 1:
	print("entspricht ca. 14 Jahre")
elif age == 2:
	print("entspricht ca. 22 Jahre")
elif age > 2:
	human = 22 + (age -2)*5
	print("Menschenjahre ", human)
# wenn man wie oben bei int etwas castenmuss wird die gesamte klammer gecastet
