for i in range(100,1000):
    sum = 0
    temp = 1
    while temp:
        sum = sum +  (temp%10) ** 3
        temp //= 10
    if sum == i:
        print(i)



print('red\yellow\tblue')
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)
    
    
