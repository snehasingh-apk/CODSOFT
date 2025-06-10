print("----- Simple Calculator -----")

# Check if a string is a number (supports +ve, -ve, decimal)
def is_number(value):
    return value.replace('.', '', 1).replace('-', '', 1).isdigit()

# Get inputs
num1_input = input("Enter first number: ")
num2_input = input("Enter second number: ")

# Check if both are valid numbers
if is_number(num1_input) and is_number(num2_input):
    num1 = float(num1_input)
    num2 = float(num2_input)

    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Floor Division (//)")
    print("7. Power (**)\n")

    operation = input("Enter operation (+, -, *, /, %, //, **): ")

    if operation == '+':
        print(f"\n✅ Result: {num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"\n✅ Result: {num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"\n✅ Result: {num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 == 0:
            print("❌ Error: Division by zero is not allowed.")
        else:
            print(f"\n✅ Result: {num1} / {num2} = {num1 / num2}")
    elif operation == '%':
        if num2 == 0:
            print("❌ Error: Modulus by zero is not allowed.")
        else:
            print(f"\n✅ Result: {num1} % {num2} = {num1 % num2}")
    elif operation == '//':
        if num2 == 0:
            print("❌ Error: Floor division by zero is not allowed.")
        else:
            print(f"\n✅ Result: {num1} // {num2} = {num1 // num2}")
    elif operation == '**':
        print(f"\n✅ Result: {num1} ** {num2} = {num1 ** num2}")
    else:
        print("❌ Invalid operation selected.")
else:
    print("❌ Invalid input. Please enter valid numbers (e.g., -5, 3.2, etc.).")
7



