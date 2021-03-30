while True:
    x = int(input("Enter a number:"))
    num = 1
    list1 = []
    while num <= x:
        if x % num == 0:
            list1.append(num)
        num = num + 1
    print(list1)
