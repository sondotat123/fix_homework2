string = input("enter a string:").lower()
letter = {}
for k in string:
    letter[k] = string.count(k)
for l in sorted(letter):
    print(l, ":", letter[l])

