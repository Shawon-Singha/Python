#for reverse printz
def value(n):
    if n == 0 : return
    print(n,end=" ")
    value(n-1)


def value(n):
    if n == 0 : return

    value(n-1)
    print(n,end= " ")

print(value(5))
print(value(5))