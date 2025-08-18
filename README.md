# Demand Forecasting ML

A complete, ready-to-upload project for predicting product demand using machine learning (XGBoost) with feature engineering for time series (lags, rolling means, calendar features).

## Project Structure
```
demand-forecasting-ml/
├─ data/
│  └─ example_demand.csv
├─ notebooks/
│  └─ Demand_Forecasting.ipynb
├─ src/
│  ├─ train.py
│  └─ utils.py
├─ models/
├─ reports/
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
```

## Dataset Format
CSV with daily rows:
- `date` (YYYY-MM-DD)
- `sku` (string, optional)
- `price` (float, optional)
- `promo` (0/1, optional)
- `demand` (integer target)

Use your own data by replacing `data/example_demand.csv` with the same column names.

## Quickstart
```bash
# 1) Create a virtual environment (optional)
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Train and forecast 30 days ahead using the example dataset
python src/train.py --data data/example_demand.csv --horizon 30 --output_dir models
```

Outputs:
- Trained model: `models/model_xgb.pkl`
- Feature config: `models/feature_info.json`
- Forecast CSV: `reports/forecast.csv`
- Metrics printed in console (MAE, RMSE, MAPE)

## Notebook
Open `notebooks/Demand_Forecasting.ipynb` for an end‑to‑end walkthrough (EDA → feature engineering → training → evaluation → forecasting with plots).

## Tips for Your Own Data
- Aggregate by day per SKU or total demand as needed.
- Add external regressors (holiday flags, marketing spend, macro indicators).
- Tune lags/rolling windows and model hyperparameters.
- Evaluate with a **time‑based** split (no shuffling).

## License
MIT


---

## 🚀 Deploy ke Streamlit Cloud (Gratis)

1. Push project ini ke GitHub (pastikan file `app.py` ada di root folder).
2. Buka [https://share.streamlit.io/](https://share.streamlit.io/) dan login dengan akun GitHub.
3. Klik **New app** → pilih repository project → branch (misal `main`) → file `app.py`.
4. Klik **Deploy**.

Setelah beberapa menit, aplikasi Anda akan tersedia secara **online gratis** dengan URL publik.

Contoh tampilan aplikasi:  
- Input tanggal, harga, dan promo.  
- Klik tombol **Prediksi**.  
- Aplikasi akan menampilkan hasil prediksi demand.

---
