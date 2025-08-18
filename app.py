import streamlit as st
import pandas as pd
import joblib
import json
from src.utils import add_calendar_features, add_lag_features, add_rolling_features

# Load model (pastikan sudah menjalankan training dulu)
try:
    model = joblib.load("models/model_xgb.pkl")
    with open("models/feature_info.json") as f:
        feature_info = json.load(f)
except:
    model = None
    feature_info = {"features": []}

st.title("📈 Demand Forecasting App")
st.write("Masukkan data untuk memprediksi permintaan barang:")

date = st.date_input("Tanggal Prediksi")
price = st.number_input("Harga Produk", value=12.5)
promo = st.selectbox("Promo?", [0, 1])

if st.button("Prediksi"):
    if model is None:
        st.error("⚠️ Model belum dilatih. Jalankan `src/train.py` dulu untuk membuat model.")
    else:
        df = pd.DataFrame([{"date": date, "price": price, "promo": promo}])
        df = add_calendar_features(df)
        df = add_lag_features(df, target="demand")
        df = add_rolling_features(df, target="demand")
        
        X = df[feature_info["features"]].fillna(0)
        yhat = model.predict(X)[0]
        
        st.success(f"📊 Prediksi Demand: {round(yhat,2)} unit")
