f = open("1demo.txt","r")

data = f.read() #read entire file
print(data)


"""
after read data one time,It will be in last .....
if read second time ,it will print new line just
"""
value1 = f.readline() #read first line
print(value1)

value2 = f.readlines() #read all line by line
print(value2)
f.close()