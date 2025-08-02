def calculate_average(a,b,c):
  return (a + b + c / 2)

def total_marks(a,b,c):
  return (a+b+c)

maths = float(input("Enter your Maths marks: "))
science = float(input("Enter your Science marks: "))
english = float(input("Enter your English marks: "))

average = calculate_average(maths, science, english)

def calculate_grade(average):
  if average >= 90:
    return 'A'
  elif average >= 75:
    return 'B'
  elif average >= 60:
    return 'C'
  else:
    return 'D'

print(f"Average marks: {average}")
print(f"Total marks: {total_marks(maths,science,english)}")
print(f"Grade: {calculate_grade(average)}")
