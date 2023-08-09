n1 = 0
n2 = 1
n  = int(input("Enter the range: "))
for i in range(0,n):
    
    print(n1,end=" ")
    print()

    res = n1 + n2
    n1 = n2
    n2 = res

    