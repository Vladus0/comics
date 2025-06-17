import telegram
from dotenv import load_dotenv
import os
from get_comic import get_comic
import argparse


def main():
    load_dotenv()
    os.makedirs('imgs', exist_ok=True)
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=token)
    filepath = "imgs/img.png"
    alt = get_comic(filepath)
    try:
        with open(f'{filepath}', 'rb') as img:
            bot.send_photo(chat_id=chat_id, photo=img, caption=alt)
    finally:
        os.remove(filepath)
    
        
if __name__=="__main__":
    main()