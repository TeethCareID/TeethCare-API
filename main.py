<<<<<<< HEAD
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow
from tensorflow import keras
import tensorflow_hub as hub
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify


model = keras.models.load_model('model-trFalse-0.8898.h5',
                                custom_objects={'KerasLayer': hub.KerasLayer})

label = ["caries", "discoloration"]

app = Flask(__name__)

def predict_label(img):
    i = np.asarray(img) / 255.0
    i = i.reshape(1, 224, 224, 3)
    pred = model.predict(i)
    result = pred[0].tolist()
    return result


@app.route("/predict", methods=["GET", "POST"])
def index():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error" : "no file"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224,224), Image.NEAREST)
    prod_img = predict_label(img)
    return prod_img

if __name__ == "__main__":
=======
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow
from tensorflow import keras
import tensorflow_hub as hub
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify


model = keras.models.load_model('model-trFalse-0.8898.h5',
                                custom_objects={'KerasLayer': hub.KerasLayer})

label = ["caries", "discoloration"]

app = Flask(__name__)

def predict_label(img):
    i = np.asarray(img) / 255.0
    i = i.reshape(1, 224, 224, 3)
    pred = model.predict(i)
    result = pred[0].tolist()
    return result


@app.route("/predict", methods=["GET", "POST"])
def index():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error" : "no file"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224,224), Image.NEAREST)
    prod_img = predict_label(img)
    return prod_img

if __name__ == "__main__":
>>>>>>> 1124035364d463322049a7ca2f3960058a856d52
    app.run(debug=True)