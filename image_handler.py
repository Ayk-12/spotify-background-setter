import urllib.request
import os

from background_changer import set_wallpaper


def get_album_image_file_name(artist: str, album: str, size: int, ext: str = ".png", sep: str = " - ") -> str:
	return ((sep.join([artist, album, f"{size}x{size}"])).replace('.', '_') + ext)


def get_wallpaper_path(artist: str, album: str) -> str:
	# returns the directory: ./ "downloaded_covers"/ artist/ album
	return (os.path.join(os.path.dirname(__file__), "downloaded_covers", artist, album))


def get_full_wallpaper_path(wallpaper_path: str, filename: str) -> str:
	# returns the file path: ./ "downloaded_covers"/ artist/ album/ imagefilename.ext
	return (os.path.join(wallpaper_path, filename))


def get_cover(url: str, artist: str, album: str, size: int, ext: str = ".png", sep: str = " - ") -> None:
	cover_name = get_album_image_file_name(artist=artist, album=album, size=size, ext=ext, sep=sep)
	path = get_wallpaper_path(artist=artist, album=album)
	full_path = get_full_wallpaper_path(wallpaper_path=path, filename=cover_name)
	
	if (not os.path.exists(path)): # download and store cover if it does not exist
		os.makedirs(path)
		urllib.request.urlretrieve(url, filename=full_path)

	set_wallpaper(wallpaper_path=full_path)
	return
