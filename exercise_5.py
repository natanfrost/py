name = 'Diamond'
age = 26
height = 180
weight = 65
hair = 'Brown'
eyes = 'Almond'

print "Let's talk about %s" % name
print "He's %d centimeter tall." % height
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)

# 1kg = 2.20lbs aproximately
print "The conversion of %dkg in lbs will be %dlbs" %(weight, weight * 2.20)

# 1cm = 0.40in aproximately
print "The conversion of %dcm in in will be %dinc" %(height, height * 0.40)

# ramdom sum
print "If i add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)
