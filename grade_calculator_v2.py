def calculate_average(a, b, c):
  return (a + b + c / 3)


def total_marks(a, b, c):
  return (a + b + c)


def get_valid_marks(subject):
  while True:
    try:
      marks = float(input(f"Enter you {subject} marks(0-100): "))
      if 0 <= marks <= 100:
        return marks
      else:
        print("Marks must be between 0 and 100, Try again!")
    except ValueError:
      print("Invalid input, please enter a number.")


maths = get_valid_marks("Maths")
science = get_valid_marks("Science")
english = get_valid_marks("English")

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
