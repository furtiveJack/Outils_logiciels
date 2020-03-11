import pickle


def dist_initial_conditions(chaine1, chaine2):
    if chaine1 == chaine2:
        return 0
    if len(chaine1) == 0:
        return len(chaine2)
    if len(chaine2) == 0:
        return len(chaine1)
    return None


def distance_substitute(chaine1, chaine2):
    dist = dist_initial_conditions(chaine1, chaine2)
    if dist is not None:
        return dist

    if chaine1[0] == chaine2[0]:
        return distance1(chaine1[1:], chaine2[1:])
    else:
        return 1 + distance1(chaine1[1:], chaine2[1:])


def distance_insert(chaine1, chaine2):
    dist = dist_initial_conditions(chaine1, chaine2)
    if dist is not None:
        return dist
    return 1 + distance1(chaine1, chaine2[1:])


def distance_delete(chaine1, chaine2):
    dist = dist_initial_conditions(chaine1, chaine2)
    if dist is not None:
        return dist
    return 1 + distance1(chaine1[1:], chaine2)


def distance1(chaine1, chaine2):
    subs = distance_substitute(chaine1, chaine2)
    ins = distance_insert(chaine1, chaine2)
    suppr = distance_delete(chaine1, chaine2)

    return min(subs, ins, suppr)


DICT_NAME = "./dictionary_memo.txt"


def distance2(chaine1, chaine2, memo):
    key = (chaine1, chaine2)
    if key in memo:
        return memo[key]
    res = distance1(chaine1, chaine2)
    memo[key] = res
    print('Added new entry ', key, ' into memory')
    return res


def closer(name, possibilities):
    closest_name = ""
    min_dist = 4096
    memo = read_memo_from_file()
    for current in possibilities:
        dist = distance2(name, current, memo)
        if dist < min_dist:
            min_dist = dist
            closest_name = current
    write_memo_to_file(memo)
    return closest_name


def write_memo_to_file(memo):
    with open(DICT_NAME, "wb") as file:
        pickle.dump(memo, file)


def read_memo_from_file():
    try:
        with open(DICT_NAME, "rb") as file:
            file_content = file.read()
            if len(file_content) == 0:
                return {}
            return pickle.loads(file_content)
    except FileNotFoundError:
        return {}

# print(distance1("bracadabra", "cabre"))
# print(distance2("abracadabra", "cabre"))
# print(distance2("bracadabra", "cssssabre"))
# print(distance2("cabre", "bracadabra"))

# print(closer("abracadabra", ["cabera", "acabre", "tata"]))
# print(closer("test", ["coucou", "non", "oui", "bien", "toto"]))
# print(closer("toto", ["coucou", "test"]))
# print(dist_memo)
