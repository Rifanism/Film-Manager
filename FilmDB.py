from Film import Film
import shelve

def filmDB(db):
    film_db = {}
    with shelve.open(db) as film:
        for title in film:
        
            director = film[title]['director']
            genre = film[title]['genre']
            year = film[title]['year']
            rating = film[title]['rating']

            theFilm = Film(title, director, genre, year, rating)
            film_db[title] = {
                'title': theFilm.title,
                'director': theFilm.director,
                'genre': theFilm.genre,
                'year': theFilm.year,
                'rating': theFilm.rating
            }
    return film_db

if __name__ == '__main__':
    myDB = filmDB('database\\films.db')
    for title in myDB:
        print(title, myDB[title]['rating'])