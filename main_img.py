from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("model_files/keras_model.h5", compile=False)

# Load the labels
class_names = open("model_files/labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
# image = Image.open("sample_data/blogimage1361284108interior-designs-for-master-bedroom.jpg").convert("RGB")
# image = Image.open("sample_data/Drawing-Room-Interior.jpg").convert("RGB")
# image = Image.open("sample_data/luxury-bedroom-interior-design-service.jpg").convert("RGB")
image = Image.open("sample_data/Watermark-7-2.jpg").convert("RGB")
# image = Image.open("sample_data/WhatsApp-Image-2020-10-19-at-22.01.25.jpeg").convert("RGB")
# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("||===================================================================||")
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)

# # print top 5
# indices = np.argsort(-data)
# print(indices)
# sorted_values = data[indices]
# top5 = sorted_values[:5]
# print(top5)
