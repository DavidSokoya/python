p = float(input('Enter principal: '))
r = float(input('Enter interest rate (eg. 50 for 50%): '))
t = float(input('Enter number of year: '))
n = float(input('Enter per year: '))


amount = p  * pow((1 + r / n), n)
 
print(f'{round(amount, 2)}')