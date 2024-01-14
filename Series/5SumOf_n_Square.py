#1*1 + 2*2 +3*3 + ...... + n*n

n = int(input("Enter the value of n:"))
sum = 0

num = range(1,n+1,1)
for x in num:
    sum = sum + x * x

print("Square Sum of 1 to",n,"is:",sum)