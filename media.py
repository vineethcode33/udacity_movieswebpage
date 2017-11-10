import webbrowser

class Movie():

	def __init__(self,movie_name, story_line, movie_poster, movie_trailer):

		self.title                 = movie_name
		self.storyline             = story_line
		self.poster_image_url      = movie_poster
		self.trailer_youtube_url   = movie_trailer