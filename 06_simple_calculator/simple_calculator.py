operator = input("Enter anoperator (+, -, * , /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':
  print(f"{num1} + {num2} = {round(num1 + num2, 2)}")
elif operator == '-':
  print(f"{num1} - {num2} = {round(num1 - num2, 2)}")
elif operator == '*':
  print(f"{num1} * {num2} = {round(num1 * num2, 2)}")
elif operator == '/':
  print(f"{num1} + {num2} = {round(num1 + num2, 2)}")
else:
    print(f"please insert a valid operator")