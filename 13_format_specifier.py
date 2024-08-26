# format specifier -> Used to control the appearance of a value when it is converted to a string.
#  Format specifiers are used in the format() method or in f-strings  

price1 = 255678999.98
price2 = -678.78
price3 = 34.67

print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:+}")
print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:+}")