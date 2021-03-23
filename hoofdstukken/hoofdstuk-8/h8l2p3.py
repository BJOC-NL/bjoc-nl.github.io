import random

list = [0] * 10
for i in range(len(list)):
    list[i] = random.randint(0, 5)


def partition_sort(list):
    if len(list) <= 1:
        return list
    else:
        turnpoint = list[0]
        head = []
        middle = []
        tail = []
        for x in list:
            if x < turnpoint:
                head.append(x)
            elif x > turnpoint:
                tail.append(x)
            else:
                middle.append(x)

        return partition_sort(head) + middle + partition_sort(tail)


print(partition_sort(list))
