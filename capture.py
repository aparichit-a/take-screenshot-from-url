import imgkit, subprocess, os, random

url = "https://www.google.com/"  # source URL

name = str(random.randrange(100, 1000000)) + "_auto_screenshot.jpg"
path = "{}/{}".format(os.path.dirname(os.path.dirname(__file__)), name)

os.makedirs(os.path.dirname(path), exist_ok=True)
# take url where you want to take screenshot and the path where you want to save it.
imgkit.from_url(url, path)
size = int(os.path.getsize(path))
