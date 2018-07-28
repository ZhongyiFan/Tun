from sys import argv
def print_none():
	print "Hello world."
def print_one(arg1):
	print arg1
def print_two(arg1,arg2):
    print arg1,arg2
def add(arg1,arg2):
	return float(arg1)+int(arg2)

script, first, second = argv
print_none()
print_one(first)
print_two(first,second)
sum = add(first,second)
print sum
