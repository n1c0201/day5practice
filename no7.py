def stringtolist(list:[str]):
    intList: [int] = []
    for i in list:
        intList.append(len(i))
    return intList
print(stringtolist(["aaaaa", "bbbbbbbb"]))