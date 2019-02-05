#Tip Calculator
#02/01/2019
#CTI-110 P2HW2-Meal Tip Calculator
#Justin Collins
#

bill = float(input("Enter total amount of the bill: "))

tip15 = bill * .15
tip18 = bill * .18
tip20 = bill * .20

print ("The amount you entered is $", format(bill, '.2f') ,sep="" )
print ("15% tip is $", format(tip15, '.2f'),sep="" )
print ("18% tip is $", format(tip18, '.2f'),sep="" )
print ("20% tip is $", format(tip20, '.2f'),sep="" )


