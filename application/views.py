from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from tensorflow.keras.models import load_model as keras_load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
import numpy as np
import os  # Ensure os module is imported for file operations

views = Blueprint('views', __name__)

# Function to load the model
def load_model():
    model_path = current_app.config.get('MODEL')
    if model_path:
        print(f"Loading model from {model_path}")
        current_app.model = keras_load_model(model_path)
    else:
        print("No model path found in configuration.")

# Run this function before handling any requests to any endpoint in the blueprint
@views.before_request
def before_request():
    load_model()

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Ensure the uploads directory exists
            if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
                os.makedirs(current_app.config['UPLOAD_FOLDER'])
            
            # Save the file to the upload folder
            filename = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            
            # Make prediction
            prediction = predict_image(filename)
            return render_template('result.html', prediction=prediction, image_url=url_for('static', filename='uploads/' + file.filename))
    return render_template('upload.html')

def predict_image(img_path):
    model = current_app.model
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust target_size to your model's input shape
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    prediction = model.predict(img_array)
    decoded_prediction = decode_predictions(prediction, top=1)[0][0]
    return decoded_prediction
