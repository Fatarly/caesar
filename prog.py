#!/usr/bin/python3

l = "abcdefghijklmnopqrstuvwxyz"

def caesar(c, n):
	if c in l:
		if l.index(c)+n < len(l):
			return l[l.index(c)+n]
		else:
			return l[l.index(c)+n-len(l)-1]
	elif c.lower() in l:
		if l.index(c.lower())+n < len(l):
			return l[l.index(c.lower())+n].upper()
		else:
			return l[l.index(c.lower())+n-len(l)-1].upper()
	else:
		return c

def st_caesar(st, n):
	r = ""
	for c in st:
		r += caesar(c, n)
	return r

def uncaesar(c, n):
	if c in l:
		if l.index(c)-n >= 0:
			return l[l.index(c)-n]
		else:
			return l[l.index(c)-n+len(l)]
	elif c.lower() in l:
		if l.index(c.lower())-n >= 0:
			return l[l.index(c.lower())-n].upper()
		else:
			return l[l.index(c.lower())-n+len(l)].upper()
	else:
		return c

def st_uncaesar(st, n):
	r = ""
	for c in st:
		r += uncaesar(c, n)
	return r

while True:
	d = input("What do you want to do? ( caesar, uncaesar ) ")
	n = int(input("How many chars do you want to push? "))

	if d.lower() == "caesar":
		with open("to_caesar/output.txt", "w") as t:
			with open("to_caesar/input.txt", "r") as f:
				for line in f:
					t.write(st_caesar(line, n))
		break
	elif d.lower() == "uncaesar":
		with open("from_caesar/output.txt", "w") as t:
                        with open("from_caesar/input.txt", "r") as f:
                                for line in f:
                                        t.write(st_uncaesar(line, n))
		break
