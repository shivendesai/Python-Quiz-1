#Written by Shiven Desai
#This program adds 10% to the gross salary
#Prompt the user to enter the gross salary and convert the input to a float
gross_salary = float(input('Enter the gross salary: '))
#Calculate the 10% bonus by multiplying the gross salary by 0.1
extra_money = gross_salary * 0.1
#Add the gross salary and bonus together to get the total salary
total_salary = gross_salary + extra_money
#Format the total salary as a string with commas and decimal places
formatted_salary = "${:,.2f}".format(total_salary)
#Print the formatted salary string as the output
print("The total salary is:", formatted_salary)