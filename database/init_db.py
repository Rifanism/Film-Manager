import shelve

if __name__ == '__main__':

    with shelve.open('films.db') as db:
        db['Twin Peaks: Fire Walk with Me'] = {
            'director': 'David Lynch',
            'genre': ['Mystery', 'Horror'],
            'year': 1992,
            'rating': 4.3
            }
        db['Fantastic Mr. Fox'] = {
            'director': 'Wes Anderson',
            'genre': ['Comedy', 'Drama'],
            'year': 2009,
            'rating': 4.3
        }
        db['The Holdovers'] = {
            'director': 'Alexander Payne',
            'genre': ['Drama', 'Comedy'],
            'year': 2023,
            'rating': 4.2
        }
        db['Paris, Texas'] = {
            'director': 'Wim Wenders',
            'genre': ['Drama', 'Family'],
            'year': 1984,
            'rating': 4.4
        }
        db['Superman'] = {
            'director': 'James Gunn',
            'genre': ['Action', 'Superhero'],
            'year': 2025,
            'rating': 3.9
        }
        db['Weapons'] = {
            'director': 'Zach Cregger',
            'genre': ['Horror', 'Mystery'],
            'year': 2025,
            'rating': 3.7
        }
        db['The Wild Robot'] = {
            'director': 'Chris Sanders',
            'genre': ['Drama', 'Adventure'],
            'year': 2024,
            'rating': 4.2
        }
        db['Conclave'] = {
            'director': 'Edward Berger',
            'genre': ['Drama', 'Thriller'],
            'year': 2024,
            'rating': 3.9
        }
        db['Longlegs'] = {
            'director': 'Osgood Perkins',
            'genre': ['Horror', 'Mystery'],
            'year': 2024,
            'rating': 3.3
        }
        db['MaXXXine'] = {
            'director': 'Ti West',
            'genre': ['Horror', 'Mystery'],
            'year': 2024,
            'rating': 3.1
        }
        db['Look Back'] = {
            'director': 'Kiyotaka Oshiyama',
            'genre': ['Drama', 'Comedy'],
            'year': 2024,
            'rating': 4.3
        }
        db['Flow'] = {
            'director': 'Gints Zilbalodis',
            'genre': ['Adventure', 'Drama'],
            'year': 2024,
            'rating': 4.1
        }
        db['Anora'] = {
            'director': 'Sean Baker',
            'genre': ['Romance', 'Drama'],
            'year': 2024,
            'rating': 3.8
        }
        db['The Substance'] = {
            'director': 'Coralie Fargeat',
            'genre': ['Horror', 'Body-Horror'],
            'year': 2024,
            'rating': 3.8
        }
        db['Kinds Of Kindness'] = {
            'director': 'Yorgos Lanthimos',
            'genre': ['Drama', 'Comedy', 'Thriller'],
            'year': 2024,
            'rating': 3.3
        }
        db['Challengers'] = {
            'director': 'Luca Guadagnino',
            'genre': ['Drama', 'Romance'],
            'year': 2023,
            'rating': 3.9
        }
        db['Civil War'] = {
            'director': 'Alex Garland',
            'genre': ['War', 'Drama'],
            'year': 2024,
            'rating': 3.5
        }
        db['Poor Things'] = {
            'director': 'Yorgos Lanthimos',
            'genre': ['Drama', 'Adventure'],
            'year': 2023,
            'rating': 4.0
        }
        db['Barbie'] = {
            'director': 'Greta Gerwig',
            'genre': ['Comedy', 'Drama'],
            'year': 2023,
            'rating': 3.7
        }
        db['Citizen Kane'] = {
            'director': 'Orson Welles',
            'genre': ['Drama', 'Mystery'],
            'year': 1941,
            'rating': 4.2
        }
        db['The Seventh Seal'] = {
            'director': 'Ingmar Bergman',
            'genre': ['Drama', 'Fantasy', 'Thriller'],
            'year': 1957,
            'rating': 4.3
        }
        db['Psycho'] = {
            'director': 'Alfred Hitchcock',
            'genre': ['Horror', 'Mystery'],
            'year': 1960,
            'rating': 4.3
        }
        db['Eraser Head'] = {
            'director': 'David Lynch',
            'genre': ['Horror', 'Body-Horror'],
            'year': 1977,
            'rating': 3.8
        }
        db['House'] = {
            'director': 'Nobuhiko Obayashi',
            'genre': ['Horror', 'Comedy'],
            'year': 1977,
            'rating': 4.0
        }
        db['Mulholland Drive'] = {
            'director': 'David Lynch',
            'genre': ['Mystery', 'Thriller'],
            'year': 2001,
            'rating': 4.3
        }