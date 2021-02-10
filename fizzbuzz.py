for i in range(1,20):
    print('{} '.format(i), end='')
    if (i%3 == 0):
        print("fizz".format(i), end='')
    if (i%5 == 0):
        print("buzz".format(i), end='')
    #if (i%3 == 0 or i%5 == 0):
    print()
