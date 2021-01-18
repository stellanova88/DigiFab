from PIL import Image
import requests


url = "https://www.yr.no/place/Norway/Viken/Halden/Halden//meteogram.png"
response = requests.get(url, stream = True)
img = Image.open(response.raw)


#TODO! Test image size 800, x
img.thumbnail((800, 262)) #Resizing

#TODO! Convert better
img = img.convert("L")

#img.show()

img.save("meteogram.png")




