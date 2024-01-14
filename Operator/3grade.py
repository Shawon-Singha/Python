marks = int(input("Enter the student's mark :"))

if marks >=0 and marks <=100:
    if marks>=80 and marks <= 100:
        print("Student get A+")

    elif marks>=70 and marks <=79:
        print("Student get A")

    elif marks>=60 and marks <= 69:
        print("Student get A-")

    elif marks>50 and marks <=59:
        print("Student get B")

    else:
        print("Sorry,you fail")
else:
    print("Input invalid")