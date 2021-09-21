import math

# 1) Heltalen från och med 1 till och med 10 i ökande ordning
i=1
while i<=10:
    print(i)
    i=i+1

# 2) Udda heltal från och med 1 till och med 49 i ökande ordning
value =range(1,51)
print(f"udda heltalet är:")
for i in value:
    if i%2 ==0:
        print()
    else:
        print(i)

# 3) Heltal från och med 10 till och med 1 i minskande ordning

list =range(1,10)
print(f"Heltal i minskande ordning:")
for i in range(1,10):
    if i(1)>i(2):
        print(i(1))



# 4) Summan av talen 7 till och med 1000
print("Summan är: ")
sum= sum(range(7,1000))
print(sum)

# 5) produkten av talen 1 till och med 1000
my_range=range(1,10)
product= math.prod(my_range)
print(f"Producten av talen är:{product}")