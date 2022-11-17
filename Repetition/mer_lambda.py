# Vad är ett lambdauttryck
# Det är en anonym funktion
import requests


def foo():
    print("Hello World")


def do_something(f):
    print("I'm the function do_something")
    print(f"Running the function {f.__name__}")
    f()
    print("Done!!!!")


def square(n):
    return n*n

if __name__ == '__main__':
    a = "En text"
    b = 12
    c = 12.5
    d = [1,2,3,4,5,6,7,8,9,10]

    questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()["questions"]

    print(questions)
    print(type(questions))

    def min_key(q):
        return q["prompt"]
#                                  Gör samma sak som funktionen min_key
    print(sorted(questions, key=lambda x: x["prompt"]))
    print(sorted(questions, key=min_key))

    print(sorted(questions, key=lambda y:int(y["times_correct"]) / int(y["times_asked"])))

    for q in sorted(questions, key=lambda y:int(y["times_correct"]) / int(y["times_asked"])):
        print(int(q["times_correct"])/int(q["times_asked"]))


#    print(list(map(square, d)))

#                      Det här talar om att vi vill skapa en anonym funktion. till skillnad från en vanlig funktion har den inget namn
#                      |  Det här är funktionens argument, motsvarar det som står inom () i en valig funktionsdef.
#                      |   |  Det här är vad funktionen gör, tänk return i en vanlig funktion
#                      |   |   |
#                      V   V   V
#     print(list(map(lambda x: x*x, d)))
#
#     print(list(filter(lambda x: x%3 == 0, d)))
#
#     f = lambda x:x**3
#
#     print("Done")
