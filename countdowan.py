import time
sec = int(input("Enter a sec"))

while sec > 0:
    print(sec)
    time.sleep(1)
    sec -= 1

print("Time's up!")