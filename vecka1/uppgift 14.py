# uppgift14.py
FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
COLOURS = ['white', 'black', 'gray']


def run():
    basket = ['volvo', 'is', 'an', 'white', 'orange', 'apple']
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