#nested dictinary
stu = {
    "name" : "Shawon",
    'sub' : {
        'Physics' : 99,
        'Math' : 98,
        'Chesmistry' : 65,
        'CSE' : 96
    },
    'Section' : '61_Q',
    'Graduation' : 2025
}
#normal print from ditionary
print(stu)

#but print dictionary inside ddictionary
print(stu['sub']['Math'])