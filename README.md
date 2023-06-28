# YouTube Shorts videos generator using ChatGPT, Bing, GTTS, OpenAI's Whisper, MoviePy and Python

## Program's Operations:

1. Read topics on which the Shorts are to be made.
2. Get text on the topic from ChatGPT API.
3. Get images as per the topic's picture description from Bing Images API.
4. Convert the text into speech using GTTS API.
5. Generate video by combining images, speech and background music using MoviePy module.
6. Get timed subtitles by transcribing the speech using OpenAI Whisper API.
7. Generate final video by attaching the subtitles.

## Run

```sh
# cd into-this-repo
# Get OpenAI API key from https://platform.openai.com/account/api-keys
# Put this key in .env.example
mv .env.example .env
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Put prompts into "config.py"
python main.py
# Generated YoutTube Shorts videos in "./shorts/"
```

## Credits

1. Downloading Pictures: https://stackoverflow.com/a/64460085/21929891
2. Generating Video: https://www.geeksforgeeks.org/convert-audio-to-video-using-static-images-in-python/
3. Burning Subtitles: https://github.com/ramsrigouthamg/Supertranslate.ai/blob/main/Burn_Subtitles_Into_Video/Burn_Subtitles_to_video_using_Moviepy.ipynb
