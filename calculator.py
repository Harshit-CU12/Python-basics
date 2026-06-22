# Simple Calculator for Beginners

print("=" * 40)
print("Welcome to Simple Calculator!")
print("=" * 40)

# Get first number from user
num1 = float(input("\nEnter first number: "))

# Get second number from user
num2 = float(input("Enter second number: "))

# Display available operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get operation choice from user
operation = input("\nEnter operation (1/2/3/4): ")

# Perform calculation based on user choice
if operation == "1":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
    
elif operation == "2":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
    
elif operation == "3":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
    
elif operation == "4":
    # Check if user is trying to divide by zero
    if num2 == 0:
        print("\nError: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
        
else:
    print("\nError: Invalid operation choice!")

print("\n" + "=" * 40)
print("Thank you for using the calculator!")
print("=" * 40)
