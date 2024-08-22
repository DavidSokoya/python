fruits = []
prices = []
total = 0


while True:
  food = input('Add fruit to the list or q to quit: ')
  if food.lower() == 'q':
      break
  else:
    price = int(input('How much is it?: '))
    fruits.append(food)
    prices.append(price)
print("...your cart'....")
for fruit in fruits:
   print(fruit, end=' ')
for price in prices:
   total += price
print()
print(f"Your total is ${total}") 