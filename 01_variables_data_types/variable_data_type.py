# VARIABLES
# Variables is a name that holds a value.
# It's like box with a label.  The value inside the box can change, hence the name "variable".

# age = 25

# print("You're " + str(age) + " yeras old")
# print("You're", age, "Years old")
# print(f"You're {age} years old")

# multiple assignment
a,b,c = 1, 2, 3
# STRINGS
name = 'David'
major = 'computer science'
school = 'Havard University'
# print(f"My name is {name}, and  I'm studying {major} at {school}.")

# INTEGERS
age = 23
year_of_admision = 2020
level = 400

# print(f"I gained admission in {year_of_admision}, and I'm now a level {level} student at the age of {age}")

# FLOAT
height = 1.67
weight = 65.9
cgpa = 4.89
# print(f"I am {height} meters tall and weigh {weight} kilograms, with a CGPA of {cgpa}")

# I am 1.67 meters tall and weigh 65.9 kilograms, with a CGPA of 5.0.

# BOOLEAN
is_fulltime_student = True
is_on_probation = False

print(f"You're a full time student? {is_fulltime_student}")
print(f"You are on probation? {is_on_probation}")

if is_fulltime_student:
  print("I am a full time student")
else: 
  print("I am a part time student")

if is_on_probation:
  print("I'm on probation")
else:
  print("I'm not on probation")


# The student's status is full-time with a scholarship awarded, and they are not on academic probation.