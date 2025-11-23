string = input("Enter any string: ")
ch = input("enter any chraracter: ")
count = 0

for i in string:
    if i == ch:
        count += 1

print(f"frequency of '{ch}' is {count}")