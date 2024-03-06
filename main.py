# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for Students in student_scores:
  highest_score+=Students

size=0
for Students in student_scores:
  size+=1

print(f"TOTALL {highest_score} {size} {highest_score/size}")

