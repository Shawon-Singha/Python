ValueList = []  
while True:
    n = input("Enter the value: ")
    
    # Convert input to an integer
    n = int(n)
    
    if n == -1:
        break
    ValueList.append(n)

print("Value is ",ValueList)