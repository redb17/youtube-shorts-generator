"""main file with algorithm to generate videos
"""
import logging
from dotenv import load_dotenv
import config
import audio
import pics
import video
import subs
import chatgpt

load_dotenv()
logging.basicConfig(
    filename='ytsg.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S')


def main():
    """main function with algorithm to generate videos
    """
    prompts = config.prompts

    for prompt in prompts:
        text_prompt = prompt['text_prompt']
        pics_prompt = prompt['pics_prompt']

        chatgpt.download_text(text_prompt)
        logging.info('>> Text downloaded')

        pics.download_pics(pics_prompt)
        logging.info('>> Pics downloaded')

        audio.text_to_audio(text_prompt)
        logging.info('>> Audio generated')

        video.audio_to_video(text_prompt, pics_prompt)
        logging.info('>> Video generated')

        subs.download_subs(text_prompt)
        logging.info('>> Subs generated')

        video.attach_subs(text_prompt)
        logging.info('>> Shorts generated')


if __name__ == "__main__":
    main()
