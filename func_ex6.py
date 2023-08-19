n = int(input())

def rec(num):
    if num == 1 or num ==0:
        return 1
    else :    
        return num*rec(num-1)



print("The factorial of " , n , " is ", rec(n))