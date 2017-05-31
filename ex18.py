# functions

# this one is like your script with argv
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r " % (arg1,arg2)

# ok, thats *args is actually pointless, we can just do this
def  print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just makes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguements
def print_none():
        print "I got nothin'."

print "print_two"
print_two("Tom", "Martin")
print "print_two_again"
print_two_again("Tom", "Martin")
print "print_one"
print_one("Just the one")
print "print_none"
print_none()
