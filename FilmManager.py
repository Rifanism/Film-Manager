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
        db = self.db
        for title in db:
            for genre in genres:
                if genre in db[title]['genre']:
                    print(f'{title} ({db[title]['year']}) | {', '.join(db[title]['genre'])} | {db[title]['rating']}')
    
    def byRating(self):
        db = self.db
        keys = list(db.keys())

        def getValue(key):
            return (-float(db[key]['rating']))
        
        def partition(low, high):
            pivotKey = keys[high]
            pivotValue = getValue(pivotKey)

            i = low - 1

            for j in range(low, high):
                currentValue = getValue(keys[j])
                if currentValue < pivotValue:
                    i = i + 1
                    keys[i], keys[j] = keys[j], keys[i]
            
            keys[i + 1], keys[high] = keys[high], keys[i + 1]
            return i + 1
        
        def recursive(low, high):
            if low < high:
                pivot = partition(low, high)
                recursive(low, pivot - 1)
                recursive(pivot + 1, high)
        
        size = len(keys)
        recursive(0, size - 1)
        return keys

if __name__ == '__main__':
    f = FilmManager()