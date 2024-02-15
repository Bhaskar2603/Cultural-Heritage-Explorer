from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf

app = Flask(__name__)

model = load_model('Monuments.h5',compile=False)

def load_and_prep_image(file, img_shape=300):
    img = tf.image.decode_image(file.read(), channels=3)
    img = tf.image.resize(img, size=[img_shape, img_shape])
    img = img / 255.
    return img

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle the image upload and make predictions
@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
       f = request.files['image']
       print(f)
       print(f.filename)
       img1 = load_and_prep_image(f.stream)
       pred = model.predict(tf.expand_dims(img1, axis=0))
       class_names=['Ajanta Caves', 'Charar-E- Sharif', 'Chhota_Imambara',
       'Ellora Caves', 'Fatehpur Sikri', 'Gateway of India',
       'Humayun_s Tomb', 'India gate pics', 'Khajuraho',
       'Sun Temple Konark', 'alai_darwaza', 'alai_minar',
       'basilica_of_bom_jesus', 'charminar', 'golden temple',
       'hawa mahal pics', 'iron_pillar', 'jamali_kamali_tomb',
       'lotus_temple', 'mysore_palace', 'qutub_minar', 'tajmahal',
       'tanjavur temple', 'victoria memorial']
       if len(pred[0]) > 1: # check for multi-class
            pred_class = class_names[pred.argmax()] # if more than one output, take the max
       else:
            pred_class = class_names[int(tf.round(pred)[0][0])]
       text=pred_class
       return text;

if __name__ == '__main__':
    app.run(debug = False, threaded = False)
