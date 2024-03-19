with open("8practice.txt","r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            num = int(num)
            if(num % 2 == 0):
                print(int(num))
            num = ""
        else:
            num += data[i]