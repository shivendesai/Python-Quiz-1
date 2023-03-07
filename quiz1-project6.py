#Written by Shiven Desai
#This program uses a while loop to calculate grades
# Ask the user to enter 4 grade scores
scores = []
for i in range(4):
    score = float(input("Enter grade score {}: ".format(i+1)))
    scores.append(score)

# Calculate the average score
average = sum(scores) / len(scores)

# Check if the average is greater than 100, and re-enter scores if necessary
while average > 100:
    print("Average score cannot be greater than 100. Please re-enter the scores.")
    scores = []
    for i in range(4):
        score = float(input("Enter grade score {}: ".format(i+1)))
        scores.append(score)
    average = sum(scores) / len(scores)

# Assign a letter grade based on the average score
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Output the letter grade
print("The average grade is {:.2f}, which corresponds to a letter grade of {}.".format(average, letter_grade))
