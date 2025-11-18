#CODE 6 & 8
num = int(input("Enter 3-digit number"))
num1 = num % 10
num2 = (num // 10) % 10     #single / se decimal me ans aayega
num3 = (num // 100)         #double // se sirf without decimal quotient aayega
print( "Sum of the digits: ", num1+num2+num3 )
print("Reverse of the number: ", (num1 * 100) + (num2 * 10) + num3)
