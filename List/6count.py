text = input("Enter the text:")

smallLeter = 0
capLetter = 0
digit = 0
numWord = 1
symbol = 0

for x in text:
    if x>='a' and x<='z':
        smallLeter = smallLeter + 1

    elif x>='A' and x<='Z':
        capLetter = capLetter+1

    elif x >= '0' and x <='9':
        digit = digit+1
    
    elif x == ' ':
        numWord = numWord +1
    else:
        symbol = symbol + 1

print("Small letter is :",smallLeter)
print("Capital letter is :",capLetter)
print("Total digit is :",digit)
print("Word is :",numWord)
print("Symbol is :",symbol)