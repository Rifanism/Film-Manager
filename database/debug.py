import init_db as db

if __name__ == '__main__':

    with db.shelve.open('films.db') as film:
        for title in film:
            print(film[title]['director'])