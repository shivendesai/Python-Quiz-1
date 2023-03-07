#Written by Shiven Desai
#This program sums and averages scores
# Prompt the user to enter 5 scores and convert each input to an integer
score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
score4 = int(input("Enter score 4: "))
score5 = int(input("Enter score 5: "))

# Calculate the sum of the 5 scores
total_score = score1 + score2 + score3 + score4 + score5

# Calculate the average of the 5 scores
average_score = total_score / 5

# Print the sum and average scores as the output
print("The total score is:", total_score)
print("The average score is:", average_score)
