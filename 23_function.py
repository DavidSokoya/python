# def sayName(name):
#   return f"Hello {name}! How are you today?"

# print(sayName('David'))
# print(sayName('John'))
# print(sayName('Ibrahim'))
# print()

# def addTwo(x, y):
#   return x + y

# def subTwo(x, y):
#   return x - y
# def mulTwo(x,y):
#   return x * y

# def divTwo(x, y):
#   return x / y

# print(addTwo(3, 5))
# print(subTwo(5, 2))
# print(mulTwo(2,3))
# print(divTwo(15,3))

# def price_list(list_price, discount = 0, tax= 0.05):
#   return list_price * (1 - discount) * (1 + tax)

# print(price_list(500))
# print(price_list(500, 0.1))
# print(price_list(500, 0.1, 0))

# import time

# def count(end,start = 0):
#   for x in range(start, end+1):
#     print(x)
#     time.sleep(1)
#   print('done')

# count(4)

# def address_list(*args):
#   for ag in args:
#     print(ag)
# address_list('London', 'Germany', 'canada', 'togo')

# def counter(*args):
#   count = 0
#   for x in args:
#     count += x
#     print(count, end=' ')

# counter(1,3,4,5,6,7)

# def print_address(**kwags):
#   for key, value in kwags.items():
#     print(f'{key}:{value}')

# print_address(str='Naira', city='Ijebu North', town='Ijebu Igbo',) 

def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=' ')
  print()
  for value in kwargs.values():
    print(value, end=' ')

shipping_label('Dr.', 'David', 'James', str = 'Nair', city ='Ijebu')