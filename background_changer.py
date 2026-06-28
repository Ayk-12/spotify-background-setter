import ctypes

from win11toast import toast


def set_background(background_path: str) -> None:
	result = ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, background_path, 0x01 | 0x02)

	if (result == 1): # success
		toast("Desktop background changed successfully.", image=background_path)
	elif (result == 0): # failure
		toast("Couldn't change desktop background.")
	return
