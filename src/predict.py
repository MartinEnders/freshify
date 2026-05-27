import sys
import numpy as np
import PIL.Image as Image
from keras.models import load_model
from keras.utils import load_img, img_to_array

IMG_SIZE = (224, 224)
MODEL_PATH = "models/pepper_classifier.keras"
MODEL = load_model(MODEL_PATH)

# Need a function for STREAMLIT
def predict(image_input):
    if isinstance(image_input, Image.Image):
        img = image_input.resize(IMG_SIZE)
    else:
        img = load_img(image_input, target_size=IMG_SIZE)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    prediction = MODEL.predict(x)[0][0]
    
    if prediction >= 0.5:
        label = "non_edible"
        confidence = float(prediction)
    else:
        label = "edible"
        confidence = float(1 - prediction)

    return label, confidence, float(prediction)