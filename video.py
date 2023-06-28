"""File with video functions.
"""
import json
from mutagen.mp3 import MP3
import imageio
from moviepy import editor
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pics


def audio_to_video(text_prompt, pics_prompt):
    """Function to generate video from audio + gif file from pictures.

    Args:
        text_prompt (String): text prompt for the video
        pics_prompt (String): description-prompt for the pictures to be downloaded
    """
    audio_filepath = './audios/' + text_prompt.replace(' ', '_') + '.mp3'
    video_filepath = './videos/' + text_prompt.replace(' ', '_') + '.mp4'
    pics_dir = './pics/' + pics_prompt.replace(' ', '_')

    list_of_images = pics.preprocess_pics(pics_dir)

    audio = MP3(audio_filepath)
    audio_length = audio.info.length
    duration = audio_length / len(list_of_images)

    # create GIF out of all the preprocessed images
    imageio.mimsave(f'{pics_dir}/pics.gif',
                    list_of_images, duration=duration * 1000)

    video = editor.VideoFileClip(f'{pics_dir}/pics.gif')
    duration = video.duration

    # background music with volume decreased to 8%
    audio_background = editor.AudioFileClip(
        'background.mp3').set_end(duration + 2.0).volumex(0.08)
    audio = editor.AudioFileClip(audio_filepath)

    composite_audio = editor.CompositeAudioClip([audio, audio_background])
    final_video = video.set_audio(composite_audio)

    final_video.write_videofile(
        fps=10,
        codec="libx264",
        filename=video_filepath)


def create_subtitle_clips(
        subtitles,
        videosize,
        fontsize=65,
        font='Arial',
        color='yellow'):
    """Create text clips with subtitles and corresponding durations.

    Args:
        subtitles (JSON): JSON object with subtitle text, start-point and end-point
        videosize (Tuple): Tuple of video width and height
        fontsize (int, optional): Size of text on the final video. Defaults to 65.
        font (str, optional): Font of text on the final video. Defaults to 'Arial'.
        color (str, optional): Colour of text on the final video. Defaults to 'yellow'.

    Returns:
        _type_: List of text clips to be 'merged' onto the final video.
    """

    subtitle_clips = []
    for subtitle in subtitles:
        start_time = subtitle['start']
        end_time = subtitle['end']
        duration = (end_time) - (start_time)

        video_width, video_height = videosize

        text_clip = TextClip(
            subtitle['text'],
            fontsize=fontsize,
            font=font,
            color=color,
            bg_color='black',
            size=(video_width * 3 / 4, None),
            method='caption') .set_start(start_time).set_duration(duration)

        subtitle_x_pos = 'center'
        subtitle_y_pos = video_height * 4 / 5

        text_clip = text_clip.set_position((subtitle_x_pos, subtitle_y_pos))
        subtitle_clips.append(text_clip)

    return subtitle_clips


def attach_subs(text_prompt):
    """Attach subtitles at appropriate timings onto the final video.

    Args:
        text_prompt (String): text prompt for the video
    """
    video_filepath = './videos/' + text_prompt.replace(' ', '_') + '.mp4'
    shorts_filepath = './shorts/' + text_prompt.replace(' ', '_') + '.mp4'
    subs_filepath = './subs/' + text_prompt.replace(' ', '_') + '.json'

    subtitles = None
    with open(subs_filepath, 'r', encoding='UTF-8') as subs_file:
        subtitles = json.load(subs_file)['segments']

    video = VideoFileClip(video_filepath)
    subtitle_clips = create_subtitle_clips(subtitles, video.size)

    final_video = CompositeVideoClip([video] + subtitle_clips)
    duration = final_video.duration

    # final video trimmed to 59 seconds which is maximum for youtube shorts
    final_video.subclip(0, min(duration - 0.5, 59)
                        ).write_videofile(shorts_filepath)
