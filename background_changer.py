import ctypes
import os

from win11toast import toast


def set_wallpaper(wallpaper_path: str) -> None:
	result = ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, wallpaper_path, 0x01 | 0x02)

	if (result == 1): # success
		toast("Desktop background changed successfully.")
	elif (result == 0):
		toast("Error while changing desktop background.")

def run_script(wallpaper_path: str, artist: str, album: str) -> None:
	curr_artitst_album_path = os.path.join(os.path.dirname(__file__), "current_wallpaper")
	new_artist_album = " - ".join([artist, album])
	try:
		f = open(curr_artitst_album_path, "x")
		f.write(new_artist_album)
		set_wallpaper(wallpaper_path=wallpaper_path)
	except FileExistsError:
		f = open(curr_artitst_album_path, "r")
		
		curr_artist_album = f.readline()
		print(f"curr artist album '{curr_artist_album}'")
		print(f"new artist album '{new_artist_album}'")
		print("are equal", new_artist_album == curr_artist_album)

		if (new_artist_album == curr_artist_album):
			toast(f"Desktop background already set to: {curr_artist_album}.")
		else:
			f.close()
			f = open(curr_artitst_album_path, "w")
			f.write(new_artist_album)
			f.close()
			set_wallpaper(wallpaper_path=wallpaper_path)
	finally:
		f.close()

	return
