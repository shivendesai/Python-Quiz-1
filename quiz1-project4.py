#Written by Shiven Desai
#This program displays sales based on commission
#User inputs a sales value
sales = float(input("Enter the sales amount: "))
#Filters through sales commissions
if 50000 <= sales <= 60000:
    commission = '10%'
    print('The commission is ' + commission)
elif 70000 <= sales <= 80000:
    commission1 = '20%'
    print('The commission is ' + commission1)
elif 90000 <= sales <= 100000:
    commission2 = '30%'
    print('The commission is ' + commission2)
else:
    print('The commission is not in a valid range')