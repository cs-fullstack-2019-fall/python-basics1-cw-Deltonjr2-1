# Python_Basics1_cw
# Problem 1:
#
# Create two variables. One should equal “My name is: “ and the other should equal your actual name. Print the two variables in one print message.
#
# Problem 2:
#
# Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.
#
# Problem 3:
#
# Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.
#
# Problem 4:
#
# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”

# 1. Ask the user to input their name

# this does not meet the requirement?
myName = input("My name is ")
yourName = input("What is your actual name?")
print(myName + " " + yourName)

# 2. Ask the user to input their extra credit points

userInput1= int(input("enter the extra credit earned "))
if  userInput1 < 5:
    print ("That's not enough")
if userInput1 > 20:
    print("That is too much")

#3 Ask user to enter a password

userInput1 = (input("Enter a password"))
print("Enter a password")
userInput2 = (input("Enter your password again"))
print("Enter your password again" )
# This should be if NOT elif AND one equal sign is variable assignment NOT comparison
if (userInput1 == userInput2):
    print("That is correct")