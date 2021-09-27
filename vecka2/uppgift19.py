import json

PHONEBOOK = "phonebook.json"


def load_phonebook():
    with open(PHONEBOOK) as f:
        return json.load(f)


def save_phonebook(pb):
    with open(PHONEBOOK, "w") as f:
        json.dump(pb, f)


def print_menu():
    print("[1] List numbers")
    print("[2] Add number")
    print("[3] Delete number")
    print("[4] Save phonebook")


def get_new_entry():
    print("New entry")
    name = input("Name>")
    number = input("Number>")
    return name, number


def main():
    phonebook = load_phonebook()

    while True:
        print_menu()
        v = input(">")
        if v == "1":
            for p in phonebook:
                print(f"{p}: {phonebook[p]}")
        elif v == "2":
            name, number = get_new_entry()
            phonebook[name] = number
        elif v == "3":
            name = input("Name to delete>")
            try:
                del phonebook[name]
            except KeyError:
                print(f"Entry {name} not found")
        elif v == "4":
            save_phonebook(phonebook)
        else:
            break


if __name__ == '__main__':
    main()
