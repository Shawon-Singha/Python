semester1 = set()
semester2 = set()

List = ['Physics','Chemistry','Math','Biology']

print("For terminate loop enter the value of -1")
i = 0
while True:
    if i == len(List): break
    x = int(input(f"Enter your first semester mark for {List[i]} : "))
    y = int(input(f"Enter your second semester mark for {List[i]} : "))

    semester1.add(x)
    semester2.add(y)
    i = i + 1

if semester1 == semester2:
    print("Going with your this form")

elif semester1 > semester2:
    print("Your first semester was good")
else:
    print("Your second semester was good")

