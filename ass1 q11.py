#Write a program to find minimum of three numbers. Use appropriate logical operators.

num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))

if num1<num2 and num1<num3:
   print("num1 is min num= ",num1)
elif num2 <num3:
 print("num2 is min num=",num2)

else:
  print("num3 is min num=",num3)
