#Answering 1(i)
animal = ['Lion','Tiger','Elephant','Giraffe','Zebra']

print(animal[:3])
print(animal[-2:])

#answering 1(ii)
def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

animal = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra']
swap(animal, 2, 4)
print(animal)

#Answering 2(i)
temperatures = [22,18,25,20,17,23,21]
print(temperatures)

#Answering 2(ii)

min_index = temperatures.index(min(temperatures))
max_index = temperatures.index(max(temperatures))

temperatures[min_index], temperatures[max_index] = temperatures[max_index], temperatures[min_index]

#Answering 2(iii)
print("Swapped temperatures:", temperatures)


#Answering 3(i)
list1 = []
list2 = []
for i in range(11,100,2):
    list1.append(i)
for j in range(3,100,3):
    list2.append(j)

common_values_set = set(list1).intersection(list2)
common_values = list(common_values_set)
print("Common values:", common_values)

#Answering 3(ii)
dictionary = dict(zip(list1, list2))

common_keys = set(list1) & set(dictionary.keys())

common_dictionary = {key: dictionary[key] for key in common_keys}

print("Common key-value pairs:", common_dictionary)




