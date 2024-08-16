# LOGICAL OPERATORS: used to make decisions based on multiple conditions

# And Operator => True if both conditions are true.
# Or Operator => True if at least one condition is true. 
# Not Operator => True if the condition is false. 


# Grade Checker
math = float(input('Enter your math score: '))
english = float(input('Enter your english score: '))


if math > 50 and english > 50:
  print('You passed!')
else:
  print('You failed!')


# Age and Height Checker
age = float(input('Enter your age: '))
height = float(input('Enter your height in cm: '))

if age > 18 and height > 150:
  print("You're eligible to enrol")
else:
  print("You're not eligible to enrol")

# Coffee Order
coffee = input('Do you want cofee? (yes / no): ')
tea = input('Do you want tea? (yes / no) ')

if coffee.lower() == 'yes' or tea.lower() == 'yes':
  print('Your order has been placed')
else:
  print('You have not placed an other')

# Book store discount checker
book = float(input('How many book would you like to buy: '))
pen = float(input('How many pen would you like to buy: '))

if book > 2 or pen > 3:
  print("You're qualified for a discount")
else:
  print("oops! you're not qualified for a discount")


# Voter Eligibility
citizen = input('Are you a citizen ofthis country? yes/no: ')

if not citizen.lower() == 'yes':
  print("You're not eligible to vote")
else:
  print("You're eligible to vote")



# Even or Odd Numbe
num = int(input('Enter a number: '))

if not num % 2 == 0:
  print("The number is odd!")
else:
  print("The number is even!")

