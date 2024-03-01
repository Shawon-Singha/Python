num = [1,2,3,4,5]

resulr = list(x for x in num if x%2 == 0)
print(resulr)

#get boolean valued
resulr = list(x%2 == 0 for x in num)
print(resulr)