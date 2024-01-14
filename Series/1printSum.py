#1+2+3.........n

n = int(input("Enter the value of n:"))
sum = 0

#num = list(range(1,n+1,1)) #if want to print list
num = range(1,n+1,1)

for x in num:
    sum = sum + x

print("Sum of 1 to",n,"is:",sum)