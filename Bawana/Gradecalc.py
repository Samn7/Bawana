#Grade calculator – Input marks → Output grade (A, B, C, etc.)
english=int(input("Enter English Marks"))
maths=int(input("Enter Maths Marks"))
chemistry=int(input("Enter Chemistry Marks"))
physics=int(input("Enter physics Marks"))
CS=int(input("Enter CS Marks"))
S=(english+maths+chemistry+physics+CS)
marks=S/5
if marks>90:
    print("A")
elif marks>=79 and marks<90:
    print("B")
elif marks>=60 and marks<79:
    print("C")
else:
    print("D")