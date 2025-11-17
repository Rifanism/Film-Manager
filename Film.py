class Film:
    def __init__(self, title, director, genre, year, rating):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.rating = rating
    
    def  __str__(self):
        return f'{self.title} ({self.year}) dir.{self.director} | {', '.join(self.genre)} | {self.rating}'
    
    def data(self):
        return {
            'title': self.title,
            'director': self.director,
            'genre': self.genre,
            'year': self.year,
            'rating': self.rating
        }