import sys
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

print("Starting script...")

IMG_SIZE = (224, 224)
MODEL_PATH = "models/pepper_classifier.keras"

if len(sys.argv) < 2:
    print("Usage: python src/predict.py <image_path>")
    sys.exit(1)

img_path = sys.argv[1]

print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)

print("Loading image...")
img = image.load_img(img_path, target_size=IMG_SIZE)

print("Converting image...")
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

print("Running prediction...")
prediction = model.predict(x)[0][0]

print("Prediction raw value:", prediction)

if prediction >= 0.5:
    label = "non_edible"
    confidence = prediction
else:
    label = "edible"
    confidence = 1 - prediction

print(f"Prediction: {label}")
print(f"Confidence: {confidence:.2%}")