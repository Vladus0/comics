import requests
import random


def get_random_comic(filepath):
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url=url)
    response.raise_for_status()
    last_comic_number = response.json()["num"]
    random_number = random.randint(0, last_comic_number)
    url = f"https://xkcd.com/{random_number}/info.0.json"
    response = requests.get(url=url)
    response.raise_for_status()
    comic_response = response.json()
    img_url = comic_response["img"]
    comics_img = requests.get(url=img_url)
    comics_img.raise_for_status()

    alt = comic_response["alt"]
    with open(filepath, 'wb') as file:
        file.write(comics_img.content)

    return alt