#-------------------------------------------------------------------------------
# Name:        warmUpAuction.py
# Purpose:
#
# Author:      Nadja Jury
#
# Created:     24/04/2014
# Copyright:   (c) juryn 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def get_float (prompt): #used to ensure input is a float
    number = 0;
    while number == 0:
        try:
            number = float(input(prompt))
        except ValueError:
            print ("I'm sorry, you need to enter a valid number")
        return number

def get_string (prompt): #used to ensure input is a string
    text = "";
    while text =="":
        try:
            text = str(input(prompt))
        except ValueError:
            print ("I'm sorry, you need to enter a valid string")
        return text

#main routine

#establishing the variables
reservePrice = 0.00
bidCount = 0
highestBid = 0.00
name = ""
bid = 0
names = []
bids = []

#entering the reserve price and telling the user the auction has begun, and how to end it
reservePrice = get_float("What is the reserve price?")
print ("The auction has now begun")
print ("If you want to end the auction, please enter 'finish' when asked for your name")

#starting the auction itself
while name!= "finish": #if the user enters F or f, the program will stop
    print ("The highest bid is currently $" + str(highestBid))
    #ask for the name and bid
    name = get_string ("What is your name?")
    if name != "finish":
        bid = get_float("What is your bid?")
        if bid > highestBid:
            highestBid = bid
            names.append(name)
            bids.append(bid)
            bidCount += 1
        else: #only accept bids that are bigger than the current highest bid
            print ("I'm sorry, " + str(name) + ", but you need to bid a higher price.")

if highestBid > reservePrice:
    print ("\nThe auction was won by " + (names[bidCount - 1]) + " with a bid of $" + str(bids[bidCount - 1]) ) #if the highest bid is higher than the reserved price, the auction is won and the winning details are displayed
else:
    print ("\nThe reserve price of $" + str(reservePrice) + " was not met.") #if the highest bid is lower than the reserved price, the auction is lost and the program tells the user that the reserve price was not met

for i in range (bidCount): #displays all the bids
    print (names[i] + " placed a bid of $" + str(bids[i]))




