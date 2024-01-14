#2+4+6+8+......+n

n = int(input("Enter the value of n:"))
sum = 0

num = range(2,n+1,2)

for x in num:
    sum = sum + x

print("SUm of Even number of 2 to",n,"is:",sum)