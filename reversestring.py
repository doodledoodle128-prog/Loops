string = input("Type your string: ")

string2 = ('')

for i in string:
    string2 = i + string2

print("\nthe original is",string)
print("\nthe new one is",string2)