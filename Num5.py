def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return True

    return False

print(overlapping((1, 5, 7, 9), (4, 6, 0, 2)))