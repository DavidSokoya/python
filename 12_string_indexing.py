# # String indexing in Python is a way to access specific characters within a string. It allows you to extract individual characters or substrings from a string by using their position or index.



# Extract the first 5 characters of a phone number

phone_number = '123-456-7890'
print(phone_number[0:5])


# Get the last 4 digits of a credit card number

credit_card_number = '1234-5678-9012-3456'
print(credit_card_number[-4:])


# Program 3: Reverse a string
name = 'David'
print(name[::-1])


#  Extract every other character from a string

str = 'abadabhdjuieeii'
print(str[::2])


#  Get the first 3 characters of a name
name = 'david'
print(name[:3])



# Email slicer

email = 'david@gmail.com'
username = email[0:email.index('@')]
domain = email[email.index('@') + 1:]


email = input('Enter your email: ')

index = email.index('@')

username = email[:index]
domain = email[index + 1: ]

print(f"Your username is: {username} and your domain is: {domain}")