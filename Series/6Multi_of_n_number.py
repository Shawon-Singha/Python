#1*2*3*4*......*n

n = int(input("Enter the value of n:"))

sum = 1

num = range(1,n+1,1)
for x in num:
    sum = sum * x

print("Multiplication of 1 to",n,"is :",sum)