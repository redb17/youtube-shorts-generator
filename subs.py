"""File to get subtitles with timestamps by using the audio file with OpenAI Whisper API
"""
import json
import whisper


def download_subs(text_prompt):
    """Function to get subtitles with timestamps by using the audio file with OpenAI Whisper API

    Args:
        text_prompt (String): text prompt for the video
    """
    audio_filepath = './audios/' + text_prompt.replace(' ', '_') + '.mp3'
    subs_filepath = './subs/' + text_prompt.replace(' ', '_') + '.json'

    model = whisper.load_model("base")
    subs = model.transcribe(audio_filepath)

    with open(subs_filepath, 'w', encoding='UTF-8') as subs_file:
        json.dump(subs, subs_file)
