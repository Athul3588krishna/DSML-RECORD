pairs = input("Enter key-value pairs: ").split()

d = dict(zip(pairs[::2], pairs[1::2]))

print("Dictionary:", d)