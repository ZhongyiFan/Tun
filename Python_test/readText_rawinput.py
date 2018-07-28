textfile = raw_input("Pls input the file name\n")
text = open(textfile)
print "The content of %s" %textfile
print text.read()
