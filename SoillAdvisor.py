print(" welcome to our Soil Advisor System!")
phvalue =float(input("Enter your soil Ph value(0-14) \n"))
if 7.5 < phvalue <= 14:
    print("PH Value : ",phvalue)
    print("Alkaline ")
    print("Add organic matter or sulfur,suitable for barley and cabbage ")
elif 5.6 <= phvalue < 7.5:
    print("PH Value : ",phvalue)
    print("Neutral ")
    print("Ideal for most crops as maize,beans and vegetables ")
elif phvalue < 5.6:
    print("PH Value : ",phvalue)
    print("Acidic ")
    print("Add agricultural lime,suitable for crops like potatoes and pineapples ")
else:
    print("Invalid soil type!,the value you entered is out of the range(0 - 14)")
    