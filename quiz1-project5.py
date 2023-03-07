#Written by Shiven Desai
#This program is an extension to project 4
# prompt user to enter sales
sales = float(input('Enter sales: $'))

# determine salary based on sales range
if sales >= 50000 and sales <= 60000:
  salary = 70000
  commission_rate = 0.1
elif sales >= 70000 and sales <= 80000:
  salary = 80000
  commission_rate = 0.2
elif sales >= 90000 and sales <= 100000:
  salary = 90000
  commission_rate = 0.3
else:
  print('Invalid sales amount entered.')
  exit()

# calculate commission and total salary
commission = sales * commission_rate
total_salary = salary + commission

# format output
formatted_sales = "${:,.2f}".format(sales)
formatted_total_salary = "${:,.2f}".format(total_salary)

# display result
print(f'For sales of {formatted_sales}, the total salary including commission is {formatted_total_salary}.')
