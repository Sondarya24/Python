from datetime import date

y1, m1, d1 = map(int, input("Enter first date(YYMMDD): ").split())
y2, m2, d2 = map(int, input("Enter second date(YYMMDD): ").split())

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)
print("Number of days: ", abs((date2 - date1).days))