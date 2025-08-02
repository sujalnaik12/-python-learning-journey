def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  if b != 0:
    return a / b
  else:
    return "Cannot divide by Zero"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operator (+, -, *, /): ")

if operation == '+':
  print(f" {num1} = {num2} = {add(num1,num2)}")
elif operation == '-':
  print(f" {num1} - {num2} = {subtract(num1,num2)}")
elif operation == '*':
  print(f" {num1} * {num2} = {multiply(num1, num2)}")
elif operation == '/':
  print(f" {num1} / {num2} = {divide(num1,num2)}")
else:
  print("Invalid operation")
