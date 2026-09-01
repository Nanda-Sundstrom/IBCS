def fun(x):
    flag = True
    i = 2
    while flag and i < len(x):
        print(flag, i, len(x), flag and i < len(x), x[i] - x[i - 1], x[i - 1] - x[i - 2])
        if x[i] - x[i - 1] != x[i - 1] - x[i - 2]:
            flag = False
        else:
            i += 1

    return flag

print(fun([7, 3, -1, -5, -8, -12]))


#The purpose of this function is to check if a list of integers have a common difference, so
#basically checking if a list of integers is an arithmetic sequence