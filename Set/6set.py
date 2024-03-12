semester1 = set()
semester2 = set()

sub_list = []

print("For terminate loop enter the value of -1")
while True:
    sub = input("Enter your subject name : ")
    if sub == '-1': break
    sub_list.append(sub)

i = 0
while True:
    if i == len(sub_list): break
    x = int(input(f"Enter your first semester mark for {sub_list[i]} : "))
    y = int(input(f"Enter your second semester mark for {sub_list[i]} : "))

    semester1.add(x)
    semester2.add(y)
    i = i + 1

if semester1 == semester2:
    print("Going with your this form")

elif semester1 < semester2:
    print("Your first semester was good")
else:
    print("Your second semester was good")

