"""ChatGPT text functions
"""
import re
import os
import openai


def download_text(text_prompt):
    """Download text-response from ChatGPT API for query in text_prompt

    Args:
        text_prompt (String): text prompt for the video
    """
    openai.api_key = os.getenv('OPENAI_KEY')

    resp = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': text_prompt
            }
        ]
    )

    text = text_prompt + '\n' + resp['choices'][0]['message']['content']

    # remove numerical bullet points which create problem in subtitles
    # alignment
    text = re.sub(r'\d+\. ', r'', text)

    text_filepath = './texts/' + text_prompt.replace(' ', '_') + '.txt'
    with open(text_filepath, 'w', encoding='UTF-8') as text_file:
        text_file.write(text)
