import random
print("Welcome to Skylink Airline!")
name = input("Enter your Name \n")
Destination = input("Enter your Destination \n")
Flightno = input("Enter the Flight Number \n")
seat = str(input("Enter Your Seat Class(Economy/ Business/ First Class) \n"))
ticketnumber= random.randint(1, 100)
if seat =='Economy':
    ticket = 8000
elif seat ==  'Business':
    ticket = 15000
elif seat == 'First Class':
    ticket = 25000
else:
    print("Invalid")
print("----------------")
print("Passenger Name ",name)
print("Flight Number ",Flightno)
print("Destination ",Destination)
print("Seat Class ",seat)
print("Ticket Number : SKY 00" + str(ticketnumber))
print("Total Cost ",ticket)