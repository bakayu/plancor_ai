from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('img_page_.html')


@app.route('/home')
def homePage():
    return render_template('index.html')


@app.route('/farmer')
def farmerPage():
    return render_template('farmer.html')


@app.route('/buyer')
def buyerPage():
    return render_template('buyer.html')


@app.route('/contact')
def contactPage():
    return render_template('contact.html')


@app.route('/product')
def prodPage():
    return render_template('product.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    global uploaded_image
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Open the image using PIL and store it in the global variable
        uploaded_image = Image.open(file_path).convert("RGB")
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
        top_col_list = []
        top_col_str = ""

        for i in range(1, 6):
            print(f"Class {i}: {class_names[top_5_r[i-1]][2:]}")
            top_col_str += f"Class {i}: {class_names[top_5_r[i-1]][2:]}"
            top_col_list.append(f"Color {i}: {class_names[top_5_r[i-1]][2:]}")
        with open(os.path.join(UPLOAD_FOLDER, 'output.txt'), 'w') as f:
            f.write(top_col_str)
        return top_col_list


if __name__ == '__main__':
    app.run(debug=True)
