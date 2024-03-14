fact = 1

n = int(input("Enter the value : "))

i = 1
while i <= n:
    fact *= i
    i+=1

print(f"Factorial of {n} is : {fact}")