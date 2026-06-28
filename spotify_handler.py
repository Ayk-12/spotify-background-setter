import spotipy
import os

from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler
from win11toast import toast
from image_handler import get_full_background_path, get_background_path, get_album_image_file_name, get_cover


def start_app() -> spotipy.Spotify:
	toast("Spotify background changer running...")

	scope = "user-read-recently-played"
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


def get_artist_album(artist: str, album: str, sep: str = " - ") -> str:
	return (sep.join([artist, album]))


def is_context_album(song_info: dict) -> bool:
	return (song_info.get("context").get("type") == "album")


def	is_new_background(artist: str, album: str, sep: str = " - ") -> bool:
	rt_change = None
	curr_artitst_album_path = os.path.join(os.path.dirname(__file__), "current_background")
	new_artist_album = get_artist_album(artist=artist, album=album)

	try:
		f = open(curr_artitst_album_path, "x")
		f.write(new_artist_album)
		f.close()
		rt_change = True # proceed to get cover
	except FileExistsError:
		f = open(curr_artitst_album_path, "r")
		curr_artist_album = f.readline()
		f.close()
		if (new_artist_album == curr_artist_album):
			rt_change = False # do not change cover
		else:
			f = open(curr_artitst_album_path, "w")
			f.write(new_artist_album)
			f.close()
			rt_change = True # proceed to get cover
	finally:
		f.close()

	return (rt_change)


def get_info_recently_played(sp_app: spotipy.Spotify) -> None:
	try:
		songs: dict = sp_app.current_user_recently_played(limit=15)
	except:
		toast("Something went wrong while connecting to Spotify...")
		return

	album_recently_played = False
	for song in songs.get("items"):
		if (is_context_album(song_info=song)):
			album_recently_played = True # now song is from an album
			break
	
	if (not album_recently_played):
		toast("Could not find any recently played album. Leaving background as is.")
		return

	all_album_covers = song.get("track").get("album").get("images")
	high_quality_index = get_highest_quality_index(all_album_covers)

	cover_url = all_album_covers[high_quality_index].get("url")
	dimensions = all_album_covers[high_quality_index].get("height")
	artist_name = (song.get("track").get("album").get("artists")[0]).get("name")
	album_name = song.get("track").get("album").get("name")

	toast(f"Latest played album: {artist_name} - {album_name}")

	if (is_new_background(artist=artist_name, album=album_name)):
		get_cover(url=cover_url, artist=artist_name, album=album_name, size=dimensions)
	else:
		toast(f"Desktop background already set to: {get_artist_album(artist=artist_name, album=album_name)}.", image=get_full_background_path(background_path=get_background_path(artist=artist_name, album=album_name), filename=get_album_image_file_name(artist=artist_name, album=album_name, size=dimensions)))
	return		


if __name__ == "__main__":
	# from pprint import pprint
	sp = start_app()
	get_info_recently_played(sp)
