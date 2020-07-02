def dri(n):
    i = n
    while True:
        n -= 3
        n += 1
        i += 1
        if n < 3:
            break
    return i
print(dri(49))

def fab(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fab(n-1) + fab(n-2)

def printfablist(n):
    for i in range(1, n+1):
        print(fab(i),end = ' ')

# printfablist(10)

def drink(n):
    count = n 
    if n >= 3:
        n = n//3 + n%3
        count = count  +drink(n)
        
    return count 

print(drink(49))
print(drink(5))
