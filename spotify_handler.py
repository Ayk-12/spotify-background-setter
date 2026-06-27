import spotipy
import os

from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler
from win11toast import toast
from image_handler import get_cover


def start_app() -> spotipy.Spotify:
	toast("Spotify background changer running...")

	scope = "user-read-currently-playing"
	try:
		cache_path = os.path.join(os.path.dirname(__file__), ".cache")
		cache_handler = CacheFileHandler(cache_path=cache_path)

		auth_manager = SpotifyOAuth(
			scope=scope,
			cache_handler=cache_handler,
			open_browser=False
		)

		sp = spotipy.Spotify(auth_manager=auth_manager)
	except:
		sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

	return (sp)


def get_highest_quality_index(data: list) -> int:
	max_ = -1
	rt_index = -1
	for i in range(len(data)):
		if (data[i].get("height") > max_):
			max_ = data[i].get("height")
			rt_index = i
	return (rt_index)


def get_playing(sp_app: spotipy.Spotify) -> None:
	song: dict = sp_app.currently_playing()
	# pprint(song)
	if (song is None):
		toast("Trying again in a bit...")
		# TODO: try again if None maybe
		return
	type_of_playback = song.get("context").get("type")
	# print(type_of_playback)
	if (type_of_playback == "album"):
		all_album_covers = song.get("item").get("album").get("images")
		high_quality_index = get_highest_quality_index(all_album_covers)

		cover_url = all_album_covers[high_quality_index].get("url")
		artist_name = (song.get("item").get("album").get("artists")[0]).get("name")
		album_name = song.get("item").get("album").get("name")

		toast(f"Playing an album: {artist_name} - {album_name}")

		get_cover(url=cover_url, artist=artist_name, album=album_name, size=all_album_covers[high_quality_index].get("height"))

	elif (type_of_playback == "playlist"):
		pass

	elif (type_of_playback is None):
		pass

	return		


if __name__ == "__main__":
	# from pprint import pprint
	sp = start_app()
	get_playing(sp)
