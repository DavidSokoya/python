# FOR LOOP ==> Execute a block of code repeatedly for a specified number of times. used to iterate over a sequence (such as a list, tuple, or string)

# names = ['David', 'Joy', 'Sam', 'Bola']
# levels = [100, 400, 300]

# for name, level in  zip(names, levels):
#   print(f"My name is {name} and I'm in {level} level")

for i in range(2):
  if i == 0:
    continue
  print(i)

name = 'David'

for letter in reversed(name):
  print(letter)

# for i in range(4):
#     for j in range(2):
#         print(f"{i} and {j}")

for i in range(1, 6):
  print(i)
print('welcometothe world!')