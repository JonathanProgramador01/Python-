# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0

for i in student_scores:
  if highest_score<i:
    highest_score=i
print(f"The highest score in the class is: {highest_score}")