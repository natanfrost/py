from sys import argv
#from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)

with open(from_file) as f: indata = f.read()

#print "The input file is %d bytes long" % len(indata)

# print "Does the outup file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

with open(to_file, 'w') as f: f.write(indata)

#print "Alright, all done."
