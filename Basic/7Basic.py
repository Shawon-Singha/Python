# a = 10
# b  = 10
# print(id(a))
# print(id(b))

# c = "Rahim"
# c.sort()

# c = list(c)
# # print(c)
# # c[0] = 'K'
# # c = "xyz ".join(c)
# # print(c)

# a = 'Shawon Singha'
# li = list(a)
# print(li[5])
# print(li[-5])

# lo = [9,14,11,'z','a','Anik','@']
# lo.sort()

# print(lo)

# seet = {1,1,2,3,4,2}  
# print(seet)

# li = [1,2,3,6,5,2,7]
# value = 3

# newList = [i for i,j in enumerate(li) if j > value]
# print(newList)

dictt1 = {'rahim': 10,'karim' : 20,'fahim' : 4}
dictt2 = {'rahim' : 12,'karim' : 2,"Sardar" : 12}

for key,value in dictt2.items():
    dictt1[key] = dictt1.get(key,0) + value

print(dictt1)