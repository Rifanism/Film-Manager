from FilmDB import filmDB, Film, shelve

path = 'database\\films.db'

class FilmManager:
    def __init__(self):
        self.db = filmDB(path)

    def add(self, title, director, genre, year, rating):
        if title in self.db:
            print(f'{title} already exists!')
            return
        with shelve.open(path) as db:
            new = Film(title, director, genre, year, rating)
            db[title] = new.data()
            print(f'{title} is successfuly added!')
    
    def remove(self, title):
        if title not in self.db:
            print('No such a film!')
            return
        with shelve.open(path) as db:
            del db[title]
            print(f'{title} is successfully removed!')
    
    def new_rating(self, title, newRate):
        with shelve.open(path) as db:
            film = db[title]
            film['rating'] = newRate
            db[title] = film
            print('Rating is successfully updated!')
    
    def showList(self):
        for title in self.db:
            director = self.db[title]['director']
            genre = self.db[title]['genre']
            year = self.db[title]['year']
            rating = self.db[title]['rating']

            film = Film(title, director, genre, year, rating)
            print(film)
    
    def byGenre(self, genres: list[str]):
        for title in self.db:
            for genre in genres:
                if genre in self.db[title]['genre']:
                    print(f'{title} | {', '.join(self.db[title]['genre'])} | {self.db[title]['rating']}')

if __name__ == '__main__':
    f = FilmManager()
    f.byGenre(['Romance'])