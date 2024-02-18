from random import seed, random
from datetime import datetime
from math import ceil, floor



def change():
    seed(datetime.now().microsecond)
    cost = ceil(random() * 100)
    all_Paid = False

    print(f"The cost is {cost}")
    amount = int(input("Enter the amount you wish to use to pay: "))

    if(amount > cost):
        amount = amount - cost
        all_Paid = True
    else:
        amount = cost - amount
    
    quarters = floor(amount / 25)
    if(quarters > 0):
        amount = amount - (floor(quarters) * 25)

    dimes = floor(amount / 10)
    if(dimes > 0):
        amount = amount - (dimes * 10)
    
    nickels = floor(amount / 5)
    if(nickels > 0):
        amount = amount - (nickels * 5)


    if(all_Paid):
        print("Your change")
        print(f"Quarter: {quarters}")
        print(f"Dimes: {dimes}")
        print(f"Nickels: {nickels}")
        print(f"Pennies: {amount}")
    else:
        print(f"You owe: {(quarters*25) + (dimes*10) + (nickels*5) + amount}")
    
    

    

    
