import requests
import random
import math


def get_comic(filepath):
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url=url)
    response.raise_for_status()
    number_last_comic = response.json()["num"]
    random_number = math.ceil(random.uniform(0, number_last_comic))
    url = f"https://xkcd.com/{random_number}/info.0.json"
    response = requests.get(url=url)
    response.raise_for_status()
    img_url = response.json()["img"]
    img = requests.get(url=img_url)
    img.raise_for_status()

    alt = response.json()["alt"]
    with open(filepath, 'wb') as file:
        file.write(img.content)

    return alt