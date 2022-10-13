char = []
name = 'JHORIZ RODEL FAJARDO AQUINO'
for n in name:
    char.append(n)

print("Characters:", char, "\n")

char.reverse()

print("Reversed Name:", end=" ")

for n in char:
    print(n, end="")