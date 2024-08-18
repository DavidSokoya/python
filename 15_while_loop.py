# WHILE LOOP ==> Executes a block of code repeatedly while condition is true

# Favorite Color 
# color = input('Enter your favorite color (q to quit): ')

# while not color == 'q':
#   print(f"Your favourite color is {color}")
#   color = input('Enter your favorite color: ')
# print("Goodbye!")


# # Guess the Number
# number = 8
# guess = int(input('Guess the number between 1 and 10: '))

# while not guess == number:
#   print("YIncorrect, try again!")
#   guess = int(input('Guess the number between 1 and 10: '))
# print("Congratulations, you guessed it!")

# # Password Validation
# original_password = 'david123'
# password = input('Enter password: ')

# while password != original_password:
#   print("Incorrect password, try again!")
#   password = input('Enter password: ')
# print('Access gained!')

# Positive Number Check
number = int(input('Enter a positive number: '))
while number <= 0:
  print("Number can't be negative")
  number = int(input('Enter a positive number: '))
print(f"You entered a positive number: {number}")

# Shopping List
item = input('Add an item to the shopping list (q to quit): ')
list = []

while item != 'q':
  list.append(item)
  item = input('Add an item to the shopping list (q to quit): ')
print(f"Your shopping list are: {list}")
