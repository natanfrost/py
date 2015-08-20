# this one is like my scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print 'arg1: %r, arg3: %r' % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print 'arg1: %r, arg3: %r' % (arg1, arg2)

#this just takes one argument

def print_one(arg1):
    print 'arg1: %r' % arg1

# this one taks no arguments

def print_none():
    print 'I got nothing.'

print_two('Killing', 'in the name of')
print_two_again('UHHHH', 'KILLING IN THE NAME OF!')
print_one('TAN NA NA NANANANA')
print_none()
