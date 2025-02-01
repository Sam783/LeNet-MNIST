import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("lenet.h5")
st.title("MNIST Digit Classifier Using LeNet")

canvas = st_canvas(
    fill_color="black",
    stroke_width=15,
    stroke_color="white",
    background_color="black",
    height=200,
    width=200,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("Predict"):
    if canvas.image_data is not None:
        img_array = canvas.image_data.astype("uint8")
        img = Image.fromarray(img_array).convert("L")
        img = img.resize((28, 28))
        img_normalized = np.array(img) / 255.0
        img_input = img_normalized.reshape(1, 28, 28, 1)

        prediction = model.predict(img_input)
        predicted_digit = np.argmax(prediction)
        st.write(f"Predicted Digit: {predicted_digit}")
        st.write("Prediction Probabilities:", prediction)