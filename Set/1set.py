num = {1,2,3,4,5,4,5}

num2 = set([4,5,6,6])
print(num2)

#add value in set
num2.add(7)
num2.add(10)
print(num2)

#remove value from set
num2.remove(10)
print(num2)

#chek the availbility
print(10 in num2)
print(7 in num2)

num2.clear()
print(num2)