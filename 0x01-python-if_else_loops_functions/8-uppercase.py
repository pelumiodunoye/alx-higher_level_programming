#!/usr/bin/python3

if ord(i) > 96 and ord(i) < 123:
		print("{:c}".format(ord(i) - 32), end="")
else:
		print(i)
