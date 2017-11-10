import media
import fresh_tomatoes

#instance of movie object
iron_man = media.Movie("IRON MAN", 
	"A billioner saves world with a robotic suit.",
	"https://images-na.ssl-images-amazon.com/images/I/71lVAGaqBtL._AC_UL320_SR212,320_.jpg",
	"https://www.youtube.com/watch?v=8hYlB38asDY")

#instance of movie object
hangover = media.Movie("The Hangover", 
	"Friends on a bachelor party.",
	"https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
	"https://www.youtube.com/watch?v=tcdUhdOlz9M")

#instance of movie object
zindagi_na_milega_dobara = media.Movie("Zindagi Na Milega Dobara", 
	"Friends on a bachelor party.(Indian version...LOL)",
	"https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Zindaginamilegidobara.jpg/220px-Zindaginamilegidobara.jpg",
	"https://www.youtube.com/watch?v=bQR_bxragHk")

#instance of movie object
thor = media.Movie("THOR", 
	"Sci-Fi movie with people from extraterestrial planets.",
	"https://i.annihil.us/u/prod/marvel/i/mg/3/a0/521f71d0689e3/portrait_incredible.jpg",
	"https://www.youtube.com/watch?v=YSC9CjSYvYA")

#instance of movie object
avatar = media.Movie("Avatar", 
	"Marine and aliens.",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

#instance of movie object
django_unchained = media.Movie("DJANGO-Unchained", 
	"Fighting against slavery and finding love.",
	"https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
	"https://www.youtube.com/watch?v=eUdM9vrCbow")

#list of instance objects
movies = [iron_man, hangover, zindagi_na_milega_dobara, thor, avatar, django_unchained]

#calling the belwo function to generate html for view
fresh_tomatoes.open_movies_page(movies)