import json
 
from imdb import Cinemagoer
# https://cinemagoer.readthedocs.io/en/latest/

# create an instance of the Cinemagoer class
ia = Cinemagoer()
 
# id
movie = ia.get_movie('0066934')
 


print(movie.data)

# print the writers
#print(writer)