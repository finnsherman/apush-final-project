
a = 0

intList = []
symbolList = []

while a == 0:
    x = input()
    if x == "+" or x == "-" or x == "*" or x == "/" or x == "^":
        symbolList.append(x)
        a+=1
    else:
        intList.append(x)
        a+=1
        