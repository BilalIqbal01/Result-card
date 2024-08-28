name:str=(input("Enter Nme:"))
Roll_number:int=(input("Enter Roll Number:"))
subject:str=(input("Enter Subject Name:"))
obtainMarks=int (input("Obtain Marks:"))
totalMarks:int=150
percentage:float=(obtainMarks/totalMarks)*100

print("\t\t\t\t\t\t***RESULT CARD**")
print("NAME:\t\tRol Number:\tSubject:\t0btain Marks:\tTotal Marks:\tPercentage:")
print(f"{name}\t{Roll_number}\t\t{subject}\t\t{obtainMarks}\t\t{totalMarks}\t\t{percentage}")
print("Final Result:")
Pass:str="PASS"
fail:str="FAIL"
if percentage >=40:
 print(f"\t\t{Pass}")
if percentage <=40:
 print(f"\t\t{fail}")
print("GRADE:")
if percentage >=90:
    print("\tA+")
elif percentage >=80:
    print("\tA")
elif percentage >=70:
    print("\tB")
elif percentage >=60:
    print("\tC")
elif percentage >=50:
    print("\tD")
elif percentage >=40:
    print("\tE")
else:
    print("\tF")