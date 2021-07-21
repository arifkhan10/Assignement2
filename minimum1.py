num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if (num1 < num2) and (num1 < num3):
   minimum = num1
elif (num2 < num1) and (num2 < num3):
   minimum = num2
else:
   minimum = num3
 
print("The minimum number is",minimum)