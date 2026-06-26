import spotipy

from spotipy.oauth2 import SpotifyOAuth
from image_handler import get_cover


def start_app() -> spotipy.Spotify:
	scope = "user-read-currently-playing"
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
		print(None)
		# TODO: try again if None maybe
		return
	type_of_playback = song.get("context").get("type")

	if (type_of_playback == "album"):
		print("PLAYING AN ALBUM")
		all_album_covers = song.get("item").get("album").get("images")
		high_quality_index = get_highest_quality_index(all_album_covers)

		cover_url = all_album_covers[high_quality_index].get("url")
		artist_name = (song.get("item").get("album").get("artists")[0]).get("name")
		album_name = song.get("item").get("album").get("name")

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
