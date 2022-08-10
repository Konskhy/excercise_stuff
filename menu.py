def add_movie():
    pass


def list_movies():
    pass


def search_movies():
    pass


menu = {
    1: ('Add movie', add_movie),
    2: ('List movies', list_movies),
    3: ('Search by title', search_movies),
    0: ('Exit program', None)
}

while True:
    for key, val in menu.items():
        print(f'{key}. {val[0]}')

    choice = int(input('\nSelect option: '))
    if choice == 0:
        break
    oper = menu[choice][1]
    oper()
