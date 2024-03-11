list1 = [3.71,3.63,3.71,3.91,3.76]

teacher = {
    'key' : 'Value',
    'result' : list1,
    'update' : {
        '6' : 4.00,
        '7' : 4.00,
        '8' : 4.00,
        '9' : 4.00
    },
    'target' : "Teacher"
}

print(teacher)
#typecast
print(list(teacher.values()))

#items means output will be in pair
print(teacher.items())
#typecast
print(list(teacher.items()))

#return the key according to value
print(teacher.get('target'))
print(teacher.get('update').get('6'))


