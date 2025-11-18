basic = float(input("ENter your basic salary"))
da = 0.40             #40% of basic salary
hra = 0.20            #20% of basic salary 
gross = basic + (da * basic) + (hra * basic)
print(gross)