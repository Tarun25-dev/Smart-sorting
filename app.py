from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img
import tensorflow as tf
import numpy as np
import os

# Load your saved multi-class model (.h5 file)
model = tf.keras.models.load_model('healthy_vs_rotten.h5')

app = Flask(__name__)

@app.route('/')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inspect')
def inspect():
    return render_template('inspect.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def output():
    if request.method == 'POST':
        f = request.files['pc_image']
        img_path = os.path.join("static/uploads", f.filename)
        f.save(img_path)

        # Load and preprocess image
        img = load_img(img_path, target_size=(224, 224))
        image_array = np.array(img)
        image_array = np.expand_dims(image_array, axis=0)

        # Predict using model
        pred = np.argmax(model.predict(image_array), axis=1)[0]

        # Map prediction to class name
        index = [
            'Apple_Healthy (0)', 'Apple_Rotten (1)', 'Banana_Healthy (2)', 'Banana_Rotten (3)',
            'Bellpepper_Healthy (4)', 'Bellpepper_Rotten (5)', 'Carrot_Healthy (6)', 'Carrot_Rotten (7)',
            'Cucumber_Healthy (8)', 'Cucumber_Rotten (9)', 'Grape_Healthy (10)', 'Grape_Rotten (11)',
            'Guava_Healthy (12)', 'Guava_Rotten (13)', 'Jujube_Healthy (14)', 'Jujube_Rotten (15)',
            'Mango_Healthy (16)', 'Mango_Rotten (17)', 'Orange_Healthy (18)', 'Orange_Rotten (19)',
            'Pomegranate_Healthy (20)', 'Pomegranate_Rotten (21)', 'Potato_Healthy (22)',
            'Potato_Rotten (23)', 'Strawberry_Healthy (24)', 'Strawberry_Rotten (25)',
            'Tomato_Healthy (26)', 'Tomato_Rotten (27)'
        ]

        prediction = index[pred]

        return render_template('portfolio-details.html', predict=prediction, img_file=f.filename)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog-single')
def blog_single():
    item = request.args.get('item')
    return render_template('blog-single.html', item=item)

if __name__ == '__main__':
    app.run(debug=True, port=2222)