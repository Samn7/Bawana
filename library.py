#Library Fine Based on Days Overdue
days = int(input (" Enter no. of days of overdue :"))
if days <= 0: 
    print (" No fine!")
elif days <= 5:
    fine = days * 2
    print (" Pay fine: Rs.", fine)
elif days <= 10:
    fine = days * 5
    print (" Pay fine: Rs.", fine)
elif days <= 30:
    fine=days * 10
    print ("Pay fine : Rs.", fine)
else:
    fine = days * 15
