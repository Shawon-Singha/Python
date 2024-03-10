list1 = [10,20,30,40] 

# #for user input, comment out thosse line

# list = []
# while  True:
#     value = int(input("Enter the value : "))
#     if value == 0:
#         movie = input("Enter your movie name : ")
#         list.append(movie)
#     elif value == 1:
#         break
#     else:
#         print("Invalid input")

update_list = ['The Godfather','Pulp Fiction','Inception','The Dark Knight'
'Titanic','Jurassic Park','The Matrix,Avatar']

info = {
    'Key' : "Value",
    '101' : "Shawon",
    '102' : "Anik",
    '103' : list1  ##passing list inside a dictionary
    
}

print(type(info))

print(info["103"])

info['103'] = update_list
print(info['103'])