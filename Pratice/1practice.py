movies = []

while  True:
    value = int(input("Enter the value : "))
    if value == 0:
        movie = input("Enter your movie name : ")
        movies.append(movie)
    elif value == 1:
        break
    else:
        print("Invalid input")


print(movies)