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
image = Image.open("sample_data/image1.jpg").convert("RGB")
# image = Image.open("sample_data/image2.jpg").convert("RGB")
# image = Image.open("sample_data/image3.jpg").convert("RGB")
# image = Image.open("sample_data/image4.jpg").convert("RGB")
# image = Image.open("sample_data/image5.jpg").convert("RGB")

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
pred_sorted = np.argsort(prediction)
top_5 = pred_sorted[0][-5:]
top_5_r = top_5[::-1]
# print("1", prediction, "2", pred_sorted)
# print("index", index)
# print("top 5", top_5)

for i in range(1, 6):
    print(f"Class {i}: {class_names[top_5_r[i-1]][2:]}")
    # print(f"Confidence Score: {prediction[0][top_5_r[i-1]]}")

# for i in pred_sorted[-5:]:
#     print(i)
#     print(class_names[i])

# Print prediction and confidence score
# print("||===================================================================||")
# print("Class:", class_name[2:], end="")
# print("Confidence Score:", confidence_score)

# # print top 5
# indices = np.argsort(-prediction)
# print(indices)
# sorted_values = class_names[indices]
# top5 = sorted_values[:5]
# print(top5)
