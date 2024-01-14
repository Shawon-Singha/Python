#4+8+12+......

n = int(input("Enter the value of n:"))
sum = 0

num = range(4,n+1,4)
for x in num:
    sum = sum + x

print("Sum of 4 t",n,"is:",sum)