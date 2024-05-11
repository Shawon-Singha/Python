'''
if user gives a confused value ,for that system will be crashed..
theb we have to handle this error..
Here we use exception handaling
'''

try:
    num1 = int(input())
    num2 = int(input())
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Division by 0 not possible")
    
except ValueError:
    print("Invalid Value")

finally:
    print("End of program")