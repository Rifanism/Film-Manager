import FilmManager as fm
import PySimpleGUIQt as qt
from os import system

app = fm.FilmManager()

def home():
    buttons = [
        [qt.Button('Display Films', size=(200, 40), font=('Poppins', 10))],
        [qt.Button('Add New Film', size=(200, 40), font=('Poppins', 10))],
        [qt.Button('Delete Film', size=(200, 40), font=('Poppins', 10))],
        [qt.Button('Change Rating', size=(200, 40), font=('Poppins', 10))],
        [qt.Button('Get Recommendations', size=(200, 40), font=('Poppins', 10))],
        [qt.Button('Exit', size=(200, 40), font=('Poppins', 10), button_color='white on red')]
    ]
    return [
        [qt.Text('Film Manager', font=('Poppins', 15), justification='center', pad=((0, 0), (0, 35)))],
        [qt.Column(buttons, element_justification='center')]
    ]

def display():
    headings = ['Title', 'Director', 'Genre', 'Year', 'Rating']
    choices = ['By Alphabet', 'By Highest Rating']
    return [
        [qt.Text('Films List', justification='center', font=('poppins', 10, 'bold'))],
        [qt.Button('Back', size=(80, 30)), 
        qt.DropDown(choices, size=(150, 25), readonly=True, key='sortedBy', enable_events=True, font=('Poppins', 10))],
        [qt.Table(
            values=app.showList(),
            headings=headings,
            num_rows=10,
            key='filmList',
            header_text_color='white',
            header_background_color='#3c3d3c',
            header_font=('Poppins', 8)
        )]
    ]

def newFilm():
    yearForm = [
        [qt.Text('Year', justification='left', pad=((70, 0), (15, 0)))],
        [qt.InputText(size=(200, 30), justification='left', pad=((72, 0), (0, 0)), key='inputYear')]
    ]
    ratingForm = [
        [qt.Text('Rating', justification='left', pad=((43, 0), (15, 0)))],
        [qt.InputText(size=(173, 30), justification='left', pad=((45, 0), (0, 0)), key='inputRating')]
    ]
    submitButton = [
        [qt.Button('Submit', size=(90, 40), key='SUBMIT')],
        [qt.Button('Back', size=(90, 40), font=('Poppins', 10), key='BACK', button_color=('white', 'red'))]
    ]
    layout = [
        [qt.Text('Insert New Film', justification='center', font=('poppins', 10, 'bold'))],
        [qt.Text('Title', justification='left', pad=((78, 0), (30, 0)))],
        [qt.InputText(size=(450, 30), justification='left', pad=((80, 0), (0, 0)), key='inputTitle')],
        [qt.Text('Director', justification='left', pad=((78, 0), (15, 0)))],
        [qt.InputText(size=(450, 30), justification='left', pad=((80, 0), (0, 0)), key='inputDir')],
        [qt.Text('Genre', justification='left', pad=((78, 0), (15, 0)))],
        [qt.InputText(size=(450, 30), justification='left', pad=((80, 0), (0, 0)), key='inputGenre')],
        [qt.Column(yearForm), qt.Column(ratingForm)],
        [qt.Column(submitButton, element_justification='center')]
    ]
    return layout

def deleteFilm():
    button = [
        [qt.Button('Delete', size=(90, 40), key='DELETE')],
        [qt.Button('Back', size=(90, 40), key='BACK', font=('Poppins', 10), button_color=('white', 'red'))]
    ]
    layout = [
        [qt.Text('Delete a Film', justification='center', font=('poppins', 10, 'bold'))],
        [qt.Text('Title', justification='left', pad=((78, 0), (80, 0)))],
        [qt.InputText(size=(450, 30), justification='left', pad=((80, 0), (0, 0)), key='deleteTitle')],
        [qt.Column(button, element_justification='center')]
    ]
    return layout

def changeRating():
    button = [
        [qt.Button('Rate', size=(90, 40), key='RATE')],
        [qt.Button('Back', size=(90, 40), key='BACK', font=('Poppins', 10), button_color=('white', 'red'))]
    ]
    layout = [
        [qt.Text('Rate a Film', justification='center', font=('poppins', 10, 'bold'))],
        [qt.Text('Title', justification='left', pad=((78, 0), (80, 0)))],
        [qt.InputText(size=(450, 30), justification='left', pad=((80, 0), (0, 0)), key='inputTitle')],
        [qt.Text('Rating', justification='left', pad=((78, 0), (15, 0)))],
        [qt.InputText(size=(450, 30), justification='left', pad=((80, 0), (0, 0)), key='inputRating')],
        [qt.Column(button, element_justification='center')]
    ]
    return layout

def recommendation():
    button = [
        [qt.Button('Generate', size=(90, 40), key='GENERATE')],
        [qt.Button('Back', size=(90, 40), key='BACK', font=('Poppins', 10), button_color=('white', 'red'))]
    ]
    layout = [
        [qt.Text('Get Recommendations', justification='center', font=('poppins', 10, 'bold'))],
        [qt.Text('Insert genres you like', justification='left', pad=((78, 0), (80, 0)))],
        [qt.InputText(size=(450, 30), justification='left', pad=((80, 0), (0, 0)), key='inputGenre')],
        [qt.Column(button, element_justification='center')]
    ]
    return layout

def recommendationResult(data: list[str]):
    headings = ['Title', 'Director', 'Genre', 'Year', 'Rating']
    return [
        [qt.Text('Films List', justification='center', font=('poppins', 10, 'bold'))],
        [qt.Button('Back', size=(80, 30), key='BACK')],
        [qt.Table(
            values=data,
            headings=headings,
            col_widths=800,
            auto_size_columns=True,
            display_row_numbers=False,
            num_rows=10,
            key='filmList'
        )]
    ]

qt.theme('Reddit')

window = qt.Window('Film Manager', home(), size=(550, 400))
current_page = 'home'

while True:
    event, values = window.read()
    if event in (qt.WIN_CLOSED, 'Exit'):
        break

    # ------ HOME PAGE ------ (Dila yang buat)
    
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
