from sys import argv
script, cats, dogs = argv
#cats = 20
#dogs = 30
if cats < dogs:
	print "More dogs than cats"
elif dogs < cats:
	print "More cats than dogs"
else:
	print "same number of cats and dogs"
