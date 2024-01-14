#1+3+5+7+.....+n

n = int(input("Enter the value of n:"))
sum = 0

num = range(1,n+1,2)
for x in num:
    sum = sum + x
print("Sum of 1 to",n,"is",sum)