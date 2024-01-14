name = input("Enter your name : ")
age =  input("Enter your age : ")
gpa = input("Enter your gpa : ")
banglaMark = input("Enter your mark :")
englishMark = input("Enter your mark :")

'''
taking input,then type cast
'''

total = int(banglaMark) + int(englishMark)
#when take input,it hold in string...for that type cast



print("\t\t\tStudent Information")
print("\t\t\t-------------------")
print("My name is " +name)
print("I am ",age, "years old")
print("My gpa is ",gpa, "& this is not enough for me")
print(name +"Total mark is:",total)


'''
type cast, when take input
'''
name = input("Enter your name : ")
age =  input("Enter your age : ")
gpa = input("Enter your gpa : ")
banglaMark = int(input("Enter your mark :"))
englishMark = int(input("Enter your mark :"))

total = banglaMark + englishMark
#when take input,it hold in string...for that type cast

print("\t\t\tStudent Information")
print("\t\t\t-------------------")
print("My name is " +name)
print("I am ",age, "years old")
print("My gpa is ",gpa, "& this is not enough for me")
print(name +"Total mark is:",total)



