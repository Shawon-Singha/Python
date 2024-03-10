list = []

while  True:
    value = int(input("Enter the value : "))
    if value == 0:
        movie = input("Enter your movie name : ")
        list.append(movie)
    elif value == 1:
        break
    else:
        print("Invalid input")

info = {
    'Key' : "Value",
    '101' : "Shawon",
    '102' : "Anik",
    '103' : list   ##passing list inside a dictionary
}

print(type(info))

print(info["103"])