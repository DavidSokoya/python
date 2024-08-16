# strings are a fundamental data type that can be manipulated using various methods. Here are some of the most commonly used string methods: upper(), lower(), capitalize(), title(), split(), join(), replace(), strip(), find(), index()

# len

# Validite use input
# 1. username is not more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12 or username.count(' ') > 0 or username.isdigit():
  print("Username is not valid")
else:
  print("Username is valid")