import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import keras

import pathlib
dataset_url = "https://drive.google.com/file/d/1iUquc-_6QWJlokfqeXdWIqAOUYy441i0/view?usp=drive_link"
archive = keras.utils.get_file(origin=dataset_url, extract=True)
data_dir = pathlib.Path(archive).with_suffix('')

image_count = len(list(data_dir.glob('*/*')))
print(image_count)
