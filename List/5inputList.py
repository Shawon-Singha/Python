n = input("Enter the text number:")

list = n.split() #in string ,get space ,count as a number
sum = 0

for num in list:
    sum = sum + int(num)

print("Sum is :",sum)
