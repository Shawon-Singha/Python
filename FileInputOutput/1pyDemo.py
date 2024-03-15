f = open("1demo.txt","r")

data = f.read() #read entire file
print(data)

value = f.readline() #read line bby line
print(value)
f.close()