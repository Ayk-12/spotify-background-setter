import urllib.request
import os

from PIL import Image
from change_background import run_script


def get_cover(url: str, artist: str, album: str, size: int, ext: str = ".png"):
	sep = " - "

	file_name = (sep.join([artist, album, f"{size}x{size}"])).replace('.', '_') + ext
	path = os.path.join(os.path.dirname(__file__), "downloaded_covers", artist, album)
	full_path = os.path.join(path, file_name)

	if not os.path.exists(path): # download and store cover if it does not exist
		print("Path does not exist; creating path at:", path)
		os.makedirs(path)
		urllib.request.urlretrieve(url, filename=full_path)

	print(full_path)
	return (run_script(full_path))
