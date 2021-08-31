import requests as req

url = "https://ghibliapi.herokuapp.com/films"

ziburi_data = req.get(url).json()
index = 2
print(ziburi_data[index]["original_title"])
print(ziburi_data[index]["director"])
print(ziburi_data[index]["producer"])
print(ziburi_data[index]["release_date"])
print(ziburi_data[index]["running_time"])
print(ziburi_data[index]["description"])
