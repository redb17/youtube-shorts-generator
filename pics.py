"""File to download pics from Bing
"""
import os
from bing_image_downloader import downloader
from PIL import Image
import numpy


def download_pics(pics_prompt):
    """Function to download pics from Bing API for Python

    Args:
        pics_prompt (String): description-prompt for the pictures to be downloaded
    """
    downloader.download(
        pics_prompt.replace(' ', '_'),
        limit=10,
        output_dir='./pics',
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        verbose=False)


def preprocess_pics(pics_dir):
    """Create list of preprocessed images.

    Args:
        pics_dir (String): Directory for images

    Returns:
        _type_: List of image objects
    """
    list_of_images = []

    for image_file in os.listdir(pics_dir):
        if image_file.endswith('.png') or image_file.endswith('.jpg'):
            image_path = os.path.join(pics_dir, image_file)
            image = Image.open(image_path).resize(
                (1080, 1920), Image.ANTIALIAS)

            shp = numpy.array(image).shape
            if len(shp) == 3 and shp[-1] == 3:
                list_of_images.append(image)

    return list_of_images
