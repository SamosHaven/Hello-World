from sys import argv

script, input_file = argv

def print_all(f):       #function that reads and prints file
    print f.read()

def rewind(f):          #function that resets file to the 0 byte (first byte)
    f.seek(0)

def print_a_line(line_count, f):        #function that goes to line and reads
    print line_count, f.readline()

current_file = open(input_file)     #current_file = main argument (input_file)

print "First lets print the whole file: \n"

print_all(current_file)     #uses print_all function to print all text in the input_file

print "Now lets rewind, kind of like a tape."

rewind(current_file)        #uses rewind function rewind input_file to start

print "Lets print three lines: "

current_line = 1
print_a_line(current_line, current_file)        #uses print_a_line function to print line 1 of input_file to start

current_line += 1
print_a_line(current_line, current_file)         #uses print_a_line function to print line 1 + 1 = 2 of input_file to start

current_line += 1
print_a_line(current_line, current_file)         #uses print_a_line function to print line 1 + 1 + 1 = 3 of input_file to start
