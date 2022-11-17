# Vad är list comprehensions
# Det är ett kompakt sätt för oss att skapa listor från någon existerande samling av ting eller generator



# Exempel med existerande samling
# Skapa en ny lista med varje element halverat
existerande_lista = [1,2,3,4,5,6,6,7,812,4,1,2]

new_list = []
for e in existerande_lista:
    new_list.append(e/2)

print(new_list)
print([e/2 for e in existerande_lista])

# samma sak fast med bara udda tal
new_filtered_list = []
for e in existerande_lista:
    if e % 2:
        new_filtered_list.append(e/2)


print(new_filtered_list)
# samma sak fast med en list comprehension med en if-sats
print([e/2 for e in existerande_lista if e%2])


print([(x, y) for x in [1,2,3] for y in [4, 5, 6] if x%2 if y%2==0])

