from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    global uploaded_image
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No file selected'
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Open the image using PIL and store it in the global variable
        uploaded_image = Image.open(file_path).convert("RGB")
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model
        model = load_model("../model_files/keras_model.h5", compile=False)

        # Load the labels
        class_names = open("../model_files/labels.txt", "r").readlines()

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        # image = Image.open("sample_data/image1.jpg").convert("RGB")
        # image = Image.open("sample_data/image2.jpg").convert("RGB")
        # image = Image.open("sample_data/image3.jpg").convert("RGB")
        # image = Image.open("sample_data/image4.jpg").convert("RGB")
        # image = Image.open("sample_data/image5.jpg").convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        uploaded_image = ImageOps.fit(uploaded_image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(uploaded_image)

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
        return f"Class: {class_name[2:]}, Confidence Score: {confidence_score}"


if __name__ == '__main__':
    app.run(debug=True)
