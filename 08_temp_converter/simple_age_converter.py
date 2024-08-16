# dob = int(input("Enter date of birth: "))
# current_year = int(input('Enter current year: '))


# age = current_year - dob
# print(f"You are {age} years old")

weight = float(input('Enter your weight in klogram (kg)): '))
height = float(input('Enter your height in meters: '))

bmi = round(weight / height, 2)

if bmi >= 30:
  print(f"Your BMI is {bmi}.. You're Obese!")
elif bmi >= 25:
  print(f"Your BMI is {bmi}.. You're overweight!")
elif bmi >= 18.5:
  print(f"Your BMI is {bmi}.. You have a normal weight!")
else:
  print(f"Your BMI is {bmi}.. You're underweight")
