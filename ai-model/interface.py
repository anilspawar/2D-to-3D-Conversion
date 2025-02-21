# ai_model/interface.py
import tensorflow as tf 
import cv2
import numpy as np 

# Load trained model
model = tf.keras.models.load_model("ai_model/feature_model.h5")

def predict_feature(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image)
    classes = ["Wall", "Pipe", "Door"]
    return classes[np.argmax(prediction)]

print(predict_feature("samples/sample_dwg.png")) 
