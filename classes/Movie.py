from .TV import TV

class Movie(TV):
    def __init__(self, title, year, rating):
        super().__init__(title, year)
        self.rating = rating
    
    def __str__(self):
        return f"{self.title}({self.year}) - Nota: {self.rating}"