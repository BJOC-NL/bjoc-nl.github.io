def comb2(numlist):
    if len(numlist) == 2:
        return [numlist]
    else:
        head = numlist[0]
        tail = numlist[1:]
        combs = []
        for x in tail:
            combs.append([head, x])
        return combs + comb2(numlist[1:])


x = [1, 2, 3, 4]
result = comb2(x)
# print(result)


def comb3(numlist):
    combs3 = []
    numlistcopy = numlist[:]
    for x in numlist:
        numlistcopy.remove(x)
        if len(numlistcopy) > 1:
            combs2 = comb2(numlistcopy)

            for y in combs2:
                result = [x] + y
                combs3.append(result)
    return combs3


x = [1, 2, 3, 4, 5, 6]

#print('comb3', comb3(x))


def comb(numlist, n):
    print('start', numlist)
    if n == 1:
        return [[x] for x in numlist]
    else:
        combs = []
        numlistcopy = numlist[:]
        for x in numlist:
            numlistcopy.remove(x)
            combs_lower = comb(numlistcopy, n-1)
            for y in combs_lower:
                result = [x] + y
                combs.append(result)
        return combs


x = [1, 2, 3, 4, 5, 6]
result = comb(x, 5)
print(result)


def comb2(numlist):
    if len(numlist) == 2:
        return [numlist]
    else:
        head = numlist[0]
        tail = numlist[1:]
        combs = []
        for x in tail:
            combs.append([head, x])
        return combs + comb2(numlist[1:])
