class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_genre(genre)
        Song.add_artist(artist)
        Song.get_genre_count(genre)
        Song.get_artist_count(artist)
        Song.count += 1

    @classmethod
    def add_genre(cls, genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_artist(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def get_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def get_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

