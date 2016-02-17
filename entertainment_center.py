# file entertainment_center.py

# coding=utf-8
import media
import fresh_tomatoes

#movie information
matrix = media.Movie("Matrix", "R",
                     "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",  # noqa
                     "A computer hacker learns from mysterious "
                     "rebels about the true nature of his reality "
                     "and his role in the war against its "
                     "controllers.",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",  # noqa
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")
matrix_reloaded = media.Movie("Matrix Reloaded", "R",
                              "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",  # noqa
                              "Neo and the rebel leaders estimate that they "
                              "have 72 hours until 250,000 probes discover "
                              "Zion and destroy it and its inhabitants. "
                              "During this, Neo must decide how he can save "
                              "Trinity from a dark fate in his dreams.",
                              "http://vignette4.wikia.nocookie.net/thegamingfamily/images/0/07/The-Matrix-Reloaded-movie-poster.jpg/revision/latest?cb=20140922193256",  # noqa
                              "https://www.youtube.com/watch?v=aOvY8NxzOjc")
matrix_revolutions = media.Movie("Matrix Revolutions", "R",
                                 "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",  # noqa
                                 "The human city of Zion defends itself "
                                 "against the massive invasion of the "
                                 "machines as Neo fights to end the "
                                 "war at another front while also "
                                 "opposing the rogue Agent Smith",
                                 "http://ayay.co.uk/movies/poster/sci_fi/the-matrix-revolutions-1.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=hMbexEPAOQI")
bourne_identity = media.Movie("The Bourne Identity", "PG-13",
                              "Franka Potente, Matt Damon, Chris Cooper",
                              "A man is picked up by a fishing boat, bullet-"
                              "riddled and suffering from amnesia, before "
                              "racing to elude assassins and regain his"
                              " memory",
                              "http://www.impawards.com/2002/posters/bourne_identity_ver2_xlg.jpg",  # noqa
                              "https://www.youtube.com/watch?v=FpKaB5dvQ4g")
the_equalizer = media.Movie("The Equalizer", "R",
                            "Denzel Washington, Marton Csokas, Chloe Grace Moretz",  # noqa
                            "What do you see when you look at me?",
                            "http://maxcdn.dardarkom.com/files/uploads/14229049191.jpg",  # noqa
                            "https://www.youtube.com/watch?v=Qt0GkVZK8zA")
john_wick = media.Movie("John Wick", "R",
                        "Keanu Reeves, Michael Nyqvist, Alfie Allen",
                        "An ex-hitman comes out of retirement to track down "
                        "the gangsters that took everything from him",
                        "http://www.newdvdreleasedates.com/images/posters/large/john-wick-2014-06.jpg",  # noqa
                        "https://www.youtube.com/watch?v=C0BMx-qxsP4")
# set the movie information
movies = [matrix, matrix_reloaded, matrix_revolutions,
          bourne_identity, the_equalizer, john_wick]
fresh_tomatoes.open_movies_page(movies)