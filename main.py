from FilmDB import filmDB
import FilmManager as fm

database = filmDB('filmdb.txt')


fm.byRating(database, False)