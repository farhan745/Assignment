def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def divid(x, y):
    return x / y

def mod(x, y):
    return x % y

try:
    print("""Select operation:
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Modulus""")
    choice_num = int(input("Enter choice (1/2/3/4/5): "))
    if choice_num >=1 and choice_num <= 5:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

      if choice_num == 1:
          print(f"{num1} + {num2} = {add(num1, num2)}")
      elif choice_num == 2:
          print(f"{num1} - {num2} = {sub(num1, num2)}")
      elif choice_num == 3:
          print(f"{num1} * {num2} = {mul(num1, num2)}")
      elif choice_num == 4:
          try:
              print(f"{num1} / {num2} = {divid(num1, num2)}")
          except ZeroDivisionError:
              print("Cannot divide by zero.")
      elif choice_num == 5:
          if num2 == 0:
              print("Error!")
              exit()
          else:
              print(f"{num1} % {num2} = {mod(num1, num2)}")
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")
      exit()

except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()
