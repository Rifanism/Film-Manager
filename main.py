from layout import *
from os import system

qt.theme('Reddit')

window = qt.Window('Film Manager', home(), size=(550, 400))
current_page = 'home'

while True:
    event, values = window.read()
    if event in (qt.WIN_CLOSED, 'Exit'):
        break

    # ------ HOME PAGE ------ (Dila yang buat)
    if current_page == 'home':
        if event == 'Display Films':
            window.close()
            window = qt.Window('Film Manager', display(), size=(550, 400))
            current_page = 'display'

        elif event == 'Add New Film':
            window.close()
            window = qt.Window('Film Manager', newFilm(), size=(550, 400))
            current_page = 'add film'
        
        elif event == 'Delete Film':
            window.close()
            window = qt.Window('Film Manager', deleteFilm(), size=(550, 400))
            current_page = 'delete film'
        elif event == 'Change Rating':
            window.close()
            window = qt.Window('Film Manager', changeRating(), size=(550, 400))
            current_page = 'change rating'
        elif event == 'Get Recommendations':
            window.close()
            window = qt.Window('Film Manager', recommendation(), size=(550, 400))
            current_page = 'get recommendations'

    # ------ DISPLAY PAGE ------ (Dila yang buat)
    elif current_page == 'display':
        if event == 'Back':
            window.close()
            window = qt.Window('Film Manager', home(), size=(550, 400))
            current_page = 'home'

        elif event == 'sortedBy':
            selected = values['sortedBy']
            if selected == 'By Highest Rating':
                window['filmList'].update(values=app.byRating())
            else:
                window['filmList'].update(values=app.showList())

    # ------ ADD FILM PAGE ------ (Senja yang buat)
    elif current_page == 'add film':
        if event == 'SUBMIT':
            title = values['inputTitle'].title()
            director = values['inputDir'].title()
            genre = [item.strip() for item in values['inputGenre'].title().split(',')]
            year = values['inputYear']
            rating = values['inputRating']
            if title == '' or director == '' or genre == '' or year == '' or rating == '':
                qt.PopupAutoClose('Fill all the blank!', background_color='red')
                continue
            insert = app.add(title, director, genre, int(year), float(rating))
            if insert:
                qt.PopupAutoClose(f'{title} is successfully added!', background_color='lightgreen')
            else:
                qt.PopupAutoClose(f'{title} is already existing!', background_color='red')
            window.close()
            system('py main.py')
            break
        elif event == 'BACK':
            window.close()
            window = qt.Window('Film Manager', home(), size=(550, 400))
            current_page = 'home'
    
    # ------ DELETE FILM PAGE ------ (Senja yang buat)
    elif current_page == 'delete film':
        if event == 'BACK':
            window.close()
            window = qt.Window('Film Manager', home(), size=(550, 400))
            current_page = 'home'
        elif event == 'DELETE':
            title = values['deleteTitle'].title()
            if title == '':
                qt.PopupAutoClose('Insert a title!', background_color='red')
                continue
            delete = app.remove(title)
            if delete:
                qt.PopupAutoClose(f'{title} is successfully removed!', background_color='lightgreen')
            else:
                qt.PopupAutoClose(f'{title} is not existing!', background_color='red')
            window.close()
            system('py main.py')
            break
    
    # ------ CHANGE RATING ------ (Restu yang buat)
    elif current_page == 'change rating':
        if event == 'BACK':
            window.close()
            window = qt.Window('Film Manager', home(), size=(550, 400))
            current_page = 'home'
        elif event == 'RATE':
            title = values['inputTitle'].title()
            newRate = values['inputRating']
            if title == '' and newRate == '':
                qt.PopupAutoClose('Fill all the blank!', background_color='red')
                continue
            new = app.newRating(title, float(newRate))
            if new:
                qt.PopupAutoClose(f' You have given {title} {newRate} stars!', background_color='lightgreen')
            else:
                qt.PopupAutoClose(f'Failed to rate {title}!', background_color='red')
            window.close()
            system('py main.py')
            break
    
    # ------ RECOMMENDATIONS ------ (Restu yang buat)
    elif current_page == 'get recommendations':
        if event == 'BACK':
            window.close()
            window = qt.Window('Film Manager', home(), size=(550, 400))
            current_page = 'home'
        elif event == 'GENERATE':
            genres = [genre.strip() for genre in values['inputGenre'].title().split(',')]
            if values['inputGenre'] == '':
                qt.PopupAutoClose('Insert genres for recommendations!', background_color='red')
                continue
            films = app.byGenre(genres)
            window.close()
            window = qt.Window('Film Manager', recommendationResult(films), size=(550, 400))
            if event == 'BACK':
                window.close()
                window = qt.Window('Film Manager', home(), size=(550, 400))
                current_page = 'home'

window.close()
