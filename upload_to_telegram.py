import telegram
from dotenv import load_dotenv
import os
from main import get_comic
import argparse


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=token)
    parser = argparse.ArgumentParser(description='Эта программа скачивает и загружает комиксы в телеграм')
    parser.add_argument('--img_path',
                        type=str, 
                        default='imgs/img.png',
                        help="Укажите куда будет сохраняться скачивемый комикс")
    args = parser.parse_args()
    alt = get_comic(args.img_path)
    try:
        with open(f'{args.img_path}', 'rb') as img:
            bot.send_photo(chat_id=chat_id, photo=img, caption=alt)
    finally:
        os.remove(args)
    
        
if __name__=="__main__":
    main()