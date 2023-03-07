#Written by Shiven Desai
#This program sums and averages scores
# Prompt the user to enter 5 scores and convert each input to an integer
score1 = int(input("Enter 60 for score 1: "))
score2 = int(input("Enter 70 for score 2: "))
score3 = int(input("Enter 80 for score 3: "))
score4 = int(input("Enter 90 for score 4: "))

# Calculate the sum of the 5 scores
total_score = score1 + score2 + score3 + score4

# Calculate the average of the 5 scores
average_score = total_score / 4

# Print the sum and average scores as the output
print("The total score is:", total_score)
print("The average score is:", average_score)

#Used 4 numbers instead of 5 because there are only 4 numbers it tells us to use