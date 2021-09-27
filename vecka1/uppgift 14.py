# uppgift14.py

FRUITS = print(input("Please enter some fruits name:"))
#['banana', 'apple', 'orange']
CARS = print(input("Please enter some cars name:"))
#['volvo', 'ford', 'tesla']
COLOURS = print(input("Please enter some colours name:"))
#['white', 'black', 'gray']


def run():
    basket = ['volvo', 'is', 'an', 'white', 'orange', 'vehicle']
    cars = []
    fruits = []
    colours = []
    rest = []
    for item in basket:
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in COLOURS:
            colours.append(item)
        else:
            rest.append(item)
            write_things(cars, 'Cars')
            write_things(fruits, 'Fruits')
            write_things(rest, 'Misc')


def write_things(items, kind):
        print(f"{kind.upper()}")
        for item in items:
                print(f" {item}")


if __name__ == '__main__':
        run()