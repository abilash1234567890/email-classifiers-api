import pickle
import os

# Load model once
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

def predict_category(text):
    return model.predict([text])[0]
