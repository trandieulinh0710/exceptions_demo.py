from guitar import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1512.9)
    print("{} get_age() - Expected {}. Got {}".format(my_guitar.name, 99, my_guitar.get_age()))
    print("{} get_age() - Expected {}.  Got {}".format(another_guitar.name, 8, another_guitar.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(my_guitar.name, True, my_guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))


main()
