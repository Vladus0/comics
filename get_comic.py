import requests
import random


def get_comic(filepath):
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url=url)
    response.raise_for_status()
    last_comic_number = response.json()["num"]
    random_number = random.randint(0, last_comic_number)
    url = f"https://xkcd.com/{random_number}/info.0.json"
    response = requests.get(url=url)
    response.raise_for_status()
    comic_responce = response.json()
    img_url = comic_responce["img"]
    comic = requests.get(url=img_url)
    comic.raise_for_status()

    alt = comic_responce["alt"]
    with open(filepath, 'wb') as file:
        file.write(comic.content)

    return alt