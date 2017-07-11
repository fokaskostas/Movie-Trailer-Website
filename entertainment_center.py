import fresh_tomatoes
import media

# Create instances of the class Movie
toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

avengers = media.Movie('Avengers',
                       'Six super-heros fight for earth',
                       'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg',
                       'https://www.youtube.com/watch?v=eOrNdBpGMv8')

matrix = media.Movie('Matrix',
                     'A computer hacker learns about the true nature of reality',
                     'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
                     'https://www.youtube.com/watch?v=m8e-FF8MsqU')

# Input of open_movies_page() function  
movies = [toy_story, avatar, avengers, matrix]

fresh_tomatoes.open_movies_page(movies)


