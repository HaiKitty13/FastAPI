from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model.pkl")

app = FastAPI(title="Abalone Rings Predictor")

class AbaloneFeatures(BaseModel):
    Sex: int        
    Length: float
    Diameter: float
    Height: float
    WholeWeight: float
    ShuckedWeight: float
    VisceraWeight: float
    ShellWeight: float

@app.post("/predict")
def predict_rings(features: AbaloneFeatures):
    data = np.array([[features.Sex, features.Length, features.Diameter,
                      features.Height, features.WholeWeight,
                      features.ShuckedWeight, features.VisceraWeight,
                      features.ShellWeight]])
    
    predicted_rings = model.predict(data)[0]

    estimated_age = predicted_rings + 1.5

    return {
        "predicted_rings": round(predicted_rings, 2),
        "estimated_age_years": round(estimated_age, 2)
    }
