from TV import TV

class series:
    def __init__(self,title,year,seasons,episodes):
        super().__init__(title,year)
        self.seasons = seasons
        self.episodes = episodes

    def __str__(self):
        return f"{self.title}({self.year}) - Temporadas: {self.seasons}, Episódios: {self.episodes}"