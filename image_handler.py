import urllib.request
import os

from PIL import Image
from background_changer import run_script


def get_cover(url: str, artist: str, album: str, size: int, ext: str = ".png") -> None:
	sep = " - "

	file_name = (sep.join([artist, album, f"{size}x{size}"])).replace('.', '_') + ext
	path = os.path.join(os.path.dirname(__file__), "downloaded_covers", artist, album)
	full_path = os.path.join(path, file_name)

	if (not os.path.exists(path)): # download and store cover if it does not exist
		os.makedirs(path)
		urllib.request.urlretrieve(url, filename=full_path)

	run_script(wallpaper_path=full_path, artist=artist, album=album)
	return
