def addi(x,y):
    def a(x,y):
        return x + y
    return a(x,y) + 5

add = addi(1,2)
print(add)
