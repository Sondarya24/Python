num1 = float(input("Enter any number"))
num2 = float(input("Enter any number"))

print(" Operations are: +, -, *, /")
op = input("choose the operation: ")

if op == '+':
    print("Answer is:", num1 + num2)
elif op == '-':
    print("Answer is:", num1 - num2)
elif op == '*':
    print("Answer is:", num1 * num2)
elif op == '/':
    print("Answer is:", num1 / num2)
else:
    print("Invalid operator.")
