print("    Student Marksheet    ")

eng = int(input("Enter the marks of english : "))
sind = int(input("Enter the marks of sindhi : "))
comp = int(input("Enter the marks of computer : "))
chemis = int(input("Enter the marks of chemistry : "))
pst = int(input("Enter the marks of Pakistan Studies : "))

print("Marks Of English =",eng)
print("Marks Of Sindhi =",sind)
print("Marks Of Computer =",comp)
print("Marks Of Chemistry =",chemis)
print("Marks Of Pakistan Studies =",pst)

obt = eng + sind + comp + chemis + pst

print("Total Marks Obtain : ",obt)

per = obt / 500 * 100

per1 = int(per)

print("Your Percentage Is : ",per1,"%")

if per>80:
 print("A++")
elif per>75:
 print("A+")
elif per>70:
 print("A")
elif per>65:
 print("B+")
elif per>60:
 print("B")
elif per>55:
 print("C+")
else:
 print("Fail")


 




