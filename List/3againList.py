subject=["Paddy","Corn","Jute","Sugar","Pulse"]

#find the length
print(len(subject))

#add item &it will add in last
subject.append("TOC")
print(subject)

#insert at specific position
subject.insert(2,"Wow")
print(subject)

#remove from list
subject.remove("TOC")
print(subject)

#remove from last
subject.pop()
print(subject)

#sort the list
subject.sort()
print(subject)

#reverse the list
subject.reverse()
print(subject)

#copy list
subject2 = subject.copy()
print(subject2)

#show index number
pos = subject.index("Corn")
print(pos)

#Count a specific number
count = subject.count("Corn")
print(count)

#clear the list
subject.clear()
print(subject)