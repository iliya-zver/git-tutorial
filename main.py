text = """Табачник Ян\n
Черемисинов"""

string = text.split("\n\n")
sorted_str = sorted(string)
print(sorted_str)

fams = []
for i in sorted_str:
    fam = i.split()[0]
    fams.append(fam)
    fams.remove()

