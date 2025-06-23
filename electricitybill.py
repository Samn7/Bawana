# Electricity Bill cenerator
units = float (input ("electricity units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1-5) + (units - 100) * 2.5
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + (units - 200) +4
else:
    bill = (100 + 1-5) + (100 * 9.5) + (100 * 4) + (units - 300) * 6
print ('Total electrity bill is :', bill )