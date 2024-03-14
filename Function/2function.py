def value(a,b,rtn_list):
    sum = a + b
    rtn_list.append(sum)
    return rtn_list

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]
rtn_list = []

for i in list1:
    for j in list2:
         hold = value(i,j,rtn_list)

print(hold)
