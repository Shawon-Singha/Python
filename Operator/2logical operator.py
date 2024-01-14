num1 =int(input("Enter the first value:"))
num2 = int(input("Enter the second value :"))
num3 = int(input("Enter the third value :"))

if num1 > num2 and num1 > num3:
   print("Maximum value is :",num1,"It's first value")

elif num2 > num1 and num2 > num3:
   print("Maximum value is :",num2,"It's second value")

else:
   print("Maximum value is:",num3,"It's third value")