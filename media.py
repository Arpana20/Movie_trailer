import webbrowser


# Getting Movie details and storing in Movie class methods
class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title     # Assigning movie_title to title
        self.poster_image_url = poster_image  # Assigning poster image URL
        self.trailer_youtube_url = trailer_youtube  # Assigning video URL
