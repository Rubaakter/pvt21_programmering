#15.1 Implementera ett program som räknar ord och bokstäver i en text
#15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com)
# och skriv ut hur många vokaler som finns i strängen. Tips: "a" in "abcd" är True!
#15.3 Göteborgsvarvet, vilken placering kom XYZ på?
# Implementera resten av detta program:
#runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
#vem = input(“Ange löpare du söker placering för”)

# runners_in_order = ["Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus"]
# who = input ("Specify runners you are looking for placement for")


text = '''Den som slänger en fimp, 
ett tuggummi eller papper på gatan ska få böter. 
Det har riksdagen bestämt. 
Det var regeringen som föreslog att den som 
skräpar ner ska kunna få böter.'''


vowels = 'aeiouyåäö'


def count_vowels(t):
    i = 0
    for letter in t:
        if letter in vowels:
            i = i+1
    return i


def count_letters(t):
    i = 0
    for letter in t:
        if letter.isalpha():
            i += 1
    return i
    # return len(t)


def count_words(t):
    return len(t.split())


#   text.split(",")
def main():

    runners_in_order = "Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus".split()
    vem = input("Specify runners you are looking for placement for")
    i = 1
    found = False
    for runner in runners_in_order:
        if runner == vem:
            print(f"{runner} kon på plats {i}")
            found = True
        i = i+1

    if not found:
        print(f"{vem} deltog inte")


def find_runner():
    runners_in_order = "Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus".split()
    vem = input("Specify runners you are looking for placement for")
    print(f"{vem} kom på plats {runners_in_order.index(vem) +1}")



if __name__ == '__main__':
    find_runner()
    # print(count_letters(text))
    # print(count_words(text))
    # print(count_vowels(text))