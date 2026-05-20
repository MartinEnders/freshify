import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

img_path = "val/non-edible/rotten_paprika6.jpeg"  # mit jeweiligem Path ersetzen

model = MobileNetV2(weights="imagenet") # Model laden, das auf ImageNet trainiert wurde

img = image.load_img(img_path, target_size=(224, 224)) #image laden und auf die benötigte Größe bringen
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x) #image ist jetzt ein input array, ready für das Model

preds = model.predict(x) # prediction machen, das Ergebnis ist ein Array mit Wahrscheinlichkeiten für jede Klasse in ImageNet
results = decode_predictions(preds, top=5)[0] # die top 5 Vorhersagen decodieren, um die tatsächlichen Labels und Scores zu erhalten

for imagenet_id, label, score in results:
    print(f"{label}: {score:.4f}")
