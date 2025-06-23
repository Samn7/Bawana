 #Bus ticket fare calculator (with age-based discount)
age=int(input("Enter your Age"))
Stops=int(input("Enter No of stations"))
gender=input("Enter your gender 'M'/'F'")
if gender == 'F':
    print("Free Ticket")
elif age<=17:
    print("Your Fair is:")
    print(Stops*7)
else:
    print("Your Fair is:")
    print(Stops*10)