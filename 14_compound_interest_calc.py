p = float(input('Enter principal: '))
r = float(input('Enter interest rate (eg. 50 for 50%): '))
t = float(input('Enter number of year: '))

while p <= 0:
  print('Principal can not be negative or zero')
  p = float(input('Enter principal: '))

while r <= 0:
  print("Rate can not be negative or zero")
  r = float(input('Enter interest rate (eg. 50 for 50%): '))

while t <= 0:
  print("Number of Year can not be negative or zero")
  t = float(input('Enter number of years): '))

amount = p  * pow((1 + (r / 100.0)), t)
 
print(f"Amount after {t} years is {round(amount, 2)}")


def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_amount(principal, rate, time):
    return principal * pow((1 + (rate / 100)), time)

def main():
    principal = get_valid_input("Enter principal: ")
    rate = get_valid_input("Enter interest rate (e.g., 50 for 50%): ")
    time = get_valid_input("Enter number of years: ")

    amount = calculate_amount(principal, rate, time)
    print(f"Amount after {time} years is {round(amount, 2)}")

if __name__ == "__main__":
    main()
