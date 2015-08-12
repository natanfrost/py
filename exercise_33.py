def while_loop_until(until):
    i = 0
    numbers = []
    while i < until:
        print "At the top i is %d" % i
        numbers.append(i)
        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    print_loop(numbers)

def for_loop_until(until):
    numbers = []
    for value in range(0, until):
        print type(value)
        print "At the top i is %d" % value
        numbers.append(value)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % (value + 1)
    print_loop(numbers)

def print_loop(numbers):
    print "The numbers: "
    for num in numbers:
        print num
