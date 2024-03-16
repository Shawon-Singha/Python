with open("6practice.txt","w") as f:
    f.write("Hi everyone\nWe are learning File I/O\n")
    f.write("using Java\nI like programming in Java")

with open("6practice.txt","r") as a:
    data = a.read()
    new_data = data.replace("Java","Python")

with open("6practice.txt","w") as b:
    b.write(new_data)

if data.find("learning"):
    print("Found")


