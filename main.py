# Code by @andrelosse

from geosearch import *


def main():

    writesearch(input("Address search -> "))

    location = searchloc(readsearch())

    print(f"Result -> {str(location[0])}")
    print(f"Coordinates: -> {str(location[1])} : {str(location[2])}")

    writecoords(location)


if __name__ == '__main__':
    main()
