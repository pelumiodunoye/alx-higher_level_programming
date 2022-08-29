#!/usr/bin/python3

for i in str:

    if ord(i) > 96 and ord(i) < 123:
		print("{:c}".format(ord(i) - 32), end="")
else:
		print(i)
