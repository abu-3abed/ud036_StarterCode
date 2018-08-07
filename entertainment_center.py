from imdb import IMDb
import media

# def __init__(self, title, storyline, poster_image, trailer_youtube)

movies = []

# toy_story = media.Movie('Toy Story',
# 					'A story of a boy and his toys that come to life',
# 					'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
# 					'https://www.youtube.com/watch?v=KYz2wyBy3kc')

# tropic_thunder = media.Movie('Tropic Thunder',
# 							'Through a series of freak occurrences, a group of actors shooting a big-budget war movie are forced to become the soldiers they are portraying.',
# 							'https://upload.wikimedia.org/wikipedia/en/d/d6/Tropic_thunder_ver3.jpg',
# 							'https://www.youtube.com/watch?v=T-6YhRZowgc')
# lord_of_the_rings = media.Movie('Lord of the Rings',
# 								'''A meek Hobbit from the Shire and eight companions 
# 								set out on a journey to destroy the powerful One 
# 								Ring and save Middle-earth from the Dark Lord Sauron.''',
# 								'https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SY999_CR0,0,673,999_AL_.jpg',
# 								'https://www.youtube.com/watch?v=V75dMMIW2B4')

# create an instance of the IMDb class
ia = IMDb()


print('note: this script would take a couple of seconds to work as it scrapes data from imdb.com website. so please be patient!')
print()
print('fetching movie (1 of 3)...',end='',flush='true')
toy_story = ia.get_movie('0114709')
print('done.')
print('fetching movie (2 of 3)...',end="",flush='true')
tropic_thunder = ia.get_movie('0942385')
print('done.')
print('fetching movie (3 of 3)...',end="",flush='true')
spirited_away = ia.get_movie('0245429')
print('done.')
print()
print('fetching movies has finished!')



# toy_story['plot outline']
movies.append(media.Movie(toy_story['long imdb title'],
					toy_story['plot outline'],
					toy_story['full-size cover url'],
					'https://www.youtube.com/watch?v=KYz2wyBy3kc'))

# TODO: continue adding movie2 & movie3 objects
# TODO: look for youtube trailer links from imdbpy

movies.append(media.Movie(tropic_thunder['long imdb title'],
							tropic_thunder['plot outline'],
							tropic_thunder['full-size cover url'],
							'https://www.youtube.com/watch?v=T-6YhRZowgc'))
movies.append(media.Movie(spirited_away['long imdb title'],
							spirited_away['plot outline'],
							spirited_away['full-size cover url'],
								'https://www.youtube.com/watch?v=ByXuk9QqQkk'))

