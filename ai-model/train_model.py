# ai_model/train_model.py 
import tensorflow as tf 
from tensorflow.keras.model import Sequential 
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense 
from tensorflow.keras.preprocessing.image import ImageDataGenerator 

# Load dataset (ensure 2D CAD dataset is available)
train_data_gen = ImageDataGenerator(rescale=1./255).flow_from_directory(
    "data/train", target_size=(224, 224), batch_size=32. class_mode="categorical"
)

# Define AI Model
model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(224, 224, 3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(3, activation="softmax")             # Three classes: walls, pipes, doors
])

# Compile and Train
model.Compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(train_data_gen, epochs=10)
model.save("ai_model/feature_model.h5")