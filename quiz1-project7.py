#Written by Shiven Desai
#This program sums the number 1-10 using a for loop
# initialize sum to 0
sum = 0

# use a for loop to iterate over the range of numbers 1-10
# range(1, 11) creates a sequence of numbers from 1 to 10 (inclusive)
# i takes the values 1, 2, ..., 10 in each iteration
for i in range(1, 11):
    # add the current number (i) to the sum
    sum += i

# print the final sum
print("The sum of the numbers 1-10 is:", sum)
