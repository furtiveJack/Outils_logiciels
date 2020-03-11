from ex2 import *
import sys

SERIES_FILE_NAME = "series_2000-2019.txt"


def create_list_from_file():
    l = []
    file = open(SERIES_FILE_NAME, "r")
    for line in file:
        l.append(line)
    file.close()
    return l


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 suggest_name.py <serie_name1 [serie_name2] ...> ")
        return
    series_list = create_list_from_file()
    print("Series list created")
    names = sys.argv[1:]
    for name in names:
        print(name, " -> ", closer(name, series_list))
    print("Done")


main()