maths = float(input("Enter your Maths marks: "))
science = float(input("Enter your Science marks: "))
english = float(input("Enter your English marks: "))

average = (maths + science + english) / 3

if average >= 90:
  grade = 'A'
elif average >= 75:
  grade = 'B'
elif average >= 60:
  grade = 'C'
else:
  grade = 'D'

print(f"Average marks: {average}")
print(f"Total marks: {maths + science + english}")
print(f"Grade: {grade}")
