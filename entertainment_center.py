from imdb import IMDb
import media


movies = []


# create an instance of the IMDb class
ia = IMDb()

# Fetching movies' data from imdb.com
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



# appending just fetched movies' data into movies list
movies.append(media.Movie(toy_story['long imdb title'],
					toy_story['plot outline'],
					toy_story['full-size cover url'],
					'https://www.youtube.com/watch?v=KYz2wyBy3kc'))


movies.append(media.Movie(tropic_thunder['long imdb title'],
							tropic_thunder['plot outline'],
							tropic_thunder['full-size cover url'],
							'https://www.youtube.com/watch?v=T-6YhRZowgc'))
movies.append(media.Movie(spirited_away['long imdb title'],
							spirited_away['plot outline'],
							spirited_away['full-size cover url'],
								'https://www.youtube.com/watch?v=ByXuk9QqQkk'))

