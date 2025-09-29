from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI()
model = joblib.load("housing_model.pkl")

expected_columns = model.feature_names_in_

class Data(BaseModel):
    OverallQual: int
    GrLivArea: int
    GarageCars: int
    TotalBsmtSF: int
    FullBath: int
    YearBuilt: int
    Neighborhood: str
    MSZoning: str
    KitchenQual: str
    CentralAir: str
    MSZoning: str


@app.get("/")
def index():
    return {"message": "Housing Prediction "}

@app.post("/predict")
def predict_price(data: Data):
    df = pd.DataFrame([data.dict()])
    df = pd.get_dummies(df)
    df = df.reindex(columns=expected_columns, fill_value=0)
    prediction = model.predict(df)
    return {"predicted_price": abs(float(prediction[0]))}

