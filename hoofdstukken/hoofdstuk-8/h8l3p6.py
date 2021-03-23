def powerset(L):
    if len(L) == 0:
        return [[]]
    else:
        operator = L[-1:]
        return powerset(L[:-1]) + [(b + operator) for b in powerset(L[:-1])]


def powerset(list):
    if len(list) == 0:
        return [[]]
    else:
        smaller_powerset = powerset(list[:-1])  # powerset of everything without last element
        operator = list[-1:]  # get last element
        result = smaller_powerset[:]  # copy the smaller powerset
        for subset in smaller_powerset:
            # finish powerset by adding the last element to each set
            result.append(subset + operator)
        return result


print(powerset([1, 2, 3]))
