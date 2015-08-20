from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input('?')

print "Opening and truncating file (if it exists) the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

formatter = "%s\n%s\n%s\n"
target.write(formatter % (line1, line2, line3))

print "And finnaly, we close it."
target.close()
