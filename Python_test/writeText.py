from sys import argv
script, textfile = argv
text = open(textfile,'w+')
line1 = "I am the GOAT\n"
text.write(line1)
print text.read()
text.close()
