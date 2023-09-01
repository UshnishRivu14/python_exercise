lst = []

def evenls():
    for i in range(4,30):
        if i%2==0:
            lst.append(i)
    return lst

print(evenls())    