"""File with audio functions.
"""
from gtts import gTTS
from pydub import AudioSegment


def text_to_audio(text_prompt):
    """Converts response-text from ChatGPT into audio file.

    Args:
        text_prompt (String): text prompt for the video
    """
    text_filepath = './texts/' + text_prompt.replace(' ', '_') + '.txt'

    text = None
    with open(text_filepath, 'r', encoding='UTF-8') as text_file:
        text = text_file.read()

    audio_filepath = './audios/' + text_prompt.replace(' ', '_') + '.mp3'
    audio_obj = gTTS(text=text, lang='en', slow=False)
    audio_obj.save(audio_filepath)

    speed = 1.25
    sound = AudioSegment.from_file(audio_filepath)

    speedup = sound.speedup(speed)
    speedup.export(audio_filepath, format='mp3')
