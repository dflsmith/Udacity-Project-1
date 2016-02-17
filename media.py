# file media.py

import webbrowser


#video class
class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


#movie class
class Movie(Video):
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_rating, movie_stars,
                 movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.rating = movie_rating
        self.stars = movie_stars
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)