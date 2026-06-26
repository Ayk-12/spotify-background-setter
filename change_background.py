import ctypes


def run_script(wallpaper_path: str) -> None:

	result = ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, wallpaper_path, 0x01 | 0x02)
	print("Result:", result)  # 1 = success, 0 = failure
