import string
import sys

SYMBOL_HEIGHT = 8
SYMBOL_WIDTH = 15
LINE_LENGTH = 80
letters = list(string.ascii_uppercase + string.ascii_lowercase)

numbers = [str(i) for i in range(10)]

symbols = [',', ';', ':', '!', '?', '.', '/', '"', '\'', '(', '-', ')', '[', '|', ']', ' ']

ascii_dict = {}


# INITIALIZATION #######################################################################################################
def init_dict() -> None:
    """
    Initialize the ascii dict by creating a key entry for all letters/numbers/symbols defined
    """
    for elem in letters:
        ascii_dict[elem] = []
    for elem in numbers:
        ascii_dict[elem] = []
    for elem in symbols:
        ascii_dict[elem] = []


def parse_file(path: string, elements: list):
    """
    Parse the file provided and add the ascii elements to the corresponding entry in the ascii dict
    :param path: path of the file to read
    :param elements: elements expected to be read in the file (in the right order)
    """
    line_count = 0
    elem_count = -1
    with open(path, "r") as file:
        for line in file:
            if line_count % 8 == 0:
                elem_count += 1
            elem = elements[elem_count]
            ascii_dict[elem].append(line[:len(line) - 1])
            line_count += 1


def init() -> None:
    """
    Initialize the ascii_dict by reading and parsing files
    """
    init_dict()
    parse_file("alphabet.txt", letters)
    parse_file("numbers.txt", numbers)
    parse_file("symbols.txt", symbols)


# ACCESS / FORMATTING ##################################################################################################
def fill_with_spaces(line: string, width: int) -> string:
    """
    Fill the line received with (len(line) - width) spaces to the right
    :param line: the string to fill with spaces
    :param width: the width we want to match when filling with spaces
    :return: the new string filled with spaces
    """
    size = len(line)
    spaces_left = width - size
    return line + (' ' * spaces_left)


def get_data(elem: string) -> list:
    """
    Return the data corresponding to the ascii representation of a character
    :param elem: element to use as a key in the ascii_dict to get its data
    :return: a list containing the data well formatted
    :raise: IndexError if the element can't be found in the ascii_dict
    """
    if elem in ascii_dict:
        max_length = len(max(ascii_dict[elem], key=len))
        if max_length == 0:
            max_length = 4
        data = []
        for s in ascii_dict[elem]:
            data.append(fill_with_spaces(s, max_length))
        return data
    else:
        raise IndexError("Unknown symbol: ", elem)


# DISPLAY ##############################################################################################################
def display_dict() -> None:
    """
    Display every value of the dict
    """
    for key in ascii_dict:
        print(key, ': ')
        for line in ascii_dict[key]:
            print(line)


# MAIN #################################################################################################################
if __name__ == '__main__':
    # Marche seulement si la chaine donnée se représente en ascii sur une seule ligne du terminal
    init()
    arg = sys.argv[1]
    sentence_data = []
    current_line = 0
    current_symbol = 0
    res = ''
    for c in arg:
        sentence_data.append(get_data(c))
    while current_line != SYMBOL_HEIGHT:
        if current_symbol == len(arg):
            current_line += 1
            current_symbol = 0
            res += '\n'
        else:
            res += sentence_data[current_symbol][current_line]
            current_symbol += 1
    print(res)
# Tentatives pour spliter la chaine ascii en plusieurs lignes
    # init()
    # arg = sys.argv[1]
    # if len(sys.argv) >= 3:
    #     line_length = int(sys.argv[2])
    # else:
    #     line_length = LINE_LENGTH
    # sentence_data = []
    # current_line = 0
    # current_symbol = 0
    # index = 0
    # next_symbol = 0
    # res = ''
    # for c in arg:
    #     sentence_data.append(get_data(c))
    #
    # line_start = 0
    # line_end = len(arg)
    #
    # for current_symbol in range(line_start, line_end):
    #     if index >= line_length:
    #         current_line += 1
    #         next_symbol = current_symbol + 1
    #         index = 0
    #         res += '\n'
    #         print(res)
    #         if current_line >= SYMBOL_HEIGHT:
    #             current_symbol = next_symbol
    #             continue
    #     else:
    #         e = sentence_data[current_symbol][current_line]
    #         index += len(e)
    #         res += e

    # while True:
    #     if index >= line_length:
    #         current_line += 1
    #         current_symbol = 0
    #         index = 0
    #         res += '\n'
    #         print(res)
    #     else:
    #         e = sentence_data[current_symbol][current_line]
    #         res += e
    #         current_symbol += 1
    #         index += len(e)

