#Height converter

height = float(input('Enter Your Height: '))
unit = input('Inches or centimeters? I or CM: ')

if unit == 'I':
  height = height * 2.54
  unit = 'cm'
  print(f'Your height is {round(height, 2)} {unit}')
elif unit == 'CM':
  height = height / 2.54
  unit = 'inches'
  print(f'Your height is {round(height, 2)} {unit}')
else:
  print(f'Input a valid unit')






