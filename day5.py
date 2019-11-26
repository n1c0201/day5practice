#1
numbers = str(input("Input numbers here:"))
numbers = numbers.replace(",", "")
newlist = numbers.split()
print("list: " + str(newlist))
print("tuple: " + str(tuple(newlist)))
