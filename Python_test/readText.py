from sys import argv
script, textfile = argv
text = open(textfile)
print "The content of %s" %textfile
#print text.read()
text1 = open("output.txt",'w')
line = text.read()
print line
text1.write(line)
text1.close()
