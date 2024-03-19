def check():
    with open("7practice.txt","r") as f:
        data = f.read()

        if(data.find('Learning')):
            print("Found")
        else:
            print("Not Found")

def check_line():
    word = "learning"
    data = True
    line_no = 1
    
    with open("7practice.txt","r") as f:
        while data:
            data == f.readline()
            if(word in data): 
                print(line_no)
                return
            line_no += 1

check()
check_line()