# creating the function with arguements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count     #prints cheese_count in sentence
    print "You have %d boxes of crackers" % boxes_of_crackers       #prints boxes_of_crackers in sentence
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# directly provide the arguements in the script
print "We can just give the function numbers directly: "
cheese_and_crackers(20,30)

# create variables in script and then use with function
print "OR, we can use variabes from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# uses a maths equation as an argument, which is solved
print "We can even do math inside too: "
cheese_and_crackers(10 + 20, 5 + 6)

# combining variables and maths in the parenthesis
print "And we can combine the two, variables and math: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
