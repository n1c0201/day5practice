def isMember(char: str, list: [str]):
    for i in list:
        if char == i:
            return True
        return False
print(isMember("a",["a", "b", "c"]))
print(isMember("a", ["g", "b", "c"]))