import media
import fresh_tomatoes

# Assigning the movie title, image url
# and video url to the objects of class Movie

# The_untold_story movie: story title,poster image,movie trailer
The_untold_story = media.Movie("M.S Dhoni:The Untold Story",
                               "https://goo.gl/AhUrAu",
                               "https://www.youtube.com/watch?v=y1FF64dIWa0")

# Taare_Zameen_par movie: story title,poster image,movie trailer
Taare_Zameen_Par = media.Movie("Taare Zameen Par",
                               "https://goo.gl/y93v2X",
                               "https://www.youtube.com/watch?v=tn_2Ie_jtX8")

# Krrish_3 movie: story title,poster image,movie trailer
Krrish_3 = media.Movie("Krrish 3",
                       "https://goo.gl/zcBErt",
                       "https://www.youtube.com/watch?v=MCCVVgtI5xU")

# Prem_Ratan_Dhan_Payo movie: story title,poster image,movie trailer
Prem_Ratan_Dhan_Payo = media.Movie("Prem Ratan Dhan Payo",
                                   "https://goo.gl/uN9ohg",
                                   "https://www.youtube.com/watch?v=bPk9bSvQQoc")  # noqa


# Creating the list to store all the objects of class movie
movies = [The_untold_story,
          Taare_Zameen_Par,
          Krrish_3,
          Prem_Ratan_Dhan_Payo]
# Sending the list to fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
