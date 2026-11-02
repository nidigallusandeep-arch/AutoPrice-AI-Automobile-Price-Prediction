import streamlit as st
import pandas as pd
import joblib
import base64
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Automobile Price Prediction",
    page_icon="🚗",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

# ---------------- BACKGROUND IMAGE ----------------
def set_background(image_path):
    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(10, 20, 40, 0.58),
                                rgba(10, 20, 40, 0.58)),
                url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .block-container {{
            padding-top: 1.8rem;
        }}

        h1, h2, h3, p, label {{
            color: white !important;
        }}

        div.stButton > button {{
            background-color: #087cf0;
            color: white;
            border-radius: 10px;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            border: none;
        }}

        div.stButton > button:hover {{
            background-color: #0055cc;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Correct background filename from your CAR folder
BACKGROUND_PATH = BASE_DIR / "car_background_streamlit.jpg"

if BACKGROUND_PATH.exists():
    set_background(BACKGROUND_PATH)
else:
    st.warning(
        "Background image not found. Put car_background_streamlit.jpg "
        "in the same folder as app.py."
    )

# ---------------- LOAD TRAINED MODEL ----------------
MODEL_PATH = BASE_DIR / "automobile_linear_regression_tuned.pkl"

if not MODEL_PATH.exists():
    st.error(
        "Model file not found: automobile_linear_regression_tuned.pkl. "
        "Copy your saved GridSearchCV Linear Regression .pkl file into the CAR folder."
    )
    st.stop()

@st.cache_resource
def load_model(path):
    return joblib.load(path)

model = load_model(str(MODEL_PATH))

# ---------------- TITLE ----------------
st.markdown(
    """
    <h1 style="text-align:center;">
        🚗 Automobile <span style="color:#2196F3;">Price Prediction</span>
    </h1>
    <p style="text-align:center;">
        Predict Used Car Selling Price Using Linear Regression
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()
st.subheader("⚙️ Enter Car Details")

# ---------------- INPUT FIELDS ----------------
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox(
        "Brand",
        ["Maruti", "Hyundai", "Tata", "Honda", "Toyota", "Mahindra",
         "Kia", "Volkswagen", "Skoda", "BMW", "Mercedes-Benz",
         "Audi", "Renault", "Ford"]
    )
    year = st.number_input("Manufacturing Year", 2008, 2026, 2021)
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric", "Hybrid"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    owner = st.selectbox("Owner Type", ["First", "Second", "Third", "Fourth or more"])
    body = st.selectbox("Body Type", ["Hatchback", "Sedan", "SUV", "MUV"])

with col2:
    km = st.number_input("Kilometers Driven", 0, 500000, 35000, step=1000)
    mileage = st.number_input("Mileage", 1.0, 600.0, 18.5, step=0.1)
    engine = st.number_input("Engine CC", 500, 6000, 1197, step=1)
    power = st.number_input("Max Power BHP", 20.0, 1000.0, 82.0, step=1.0)
    seats = st.selectbox("Seats", [4, 5, 6, 7, 8])

st.divider()

# ---------------- PREDICTION ----------------
if st.button("🚀 Predict Selling Price", use_container_width=True):
    input_data = pd.DataFrame([{
        "Brand": brand,
        "Year": year,
        "Fuel_Type": fuel,
        "Transmission": transmission,
        "Owner_Type": owner,
        "Body_Type": body,
        "Kilometers_Driven": km,
        "Mileage": mileage,
        "Engine_CC": engine,
        "Max_Power_BHP": power,
        "Seats": seats
    }])

    try:
        prediction = float(model.predict(input_data)[0])
        st.success(f"🚗 Predicted Selling Price: ₹ {prediction:.2f} Lakhs")
        st.caption("This is an estimated model prediction, not a guaranteed market price.")
        st.balloons()
    except Exception as error:
        st.error(f"Prediction error: {error}")
        st.info(
            "Check that this model was trained with the same 11 input columns "
            "and preprocessing pipeline."
        )

# ---------------- FOOTER ----------------
st.markdown(
    """
    <hr>
    <p style="text-align:center;">
        Developed using Python | Scikit-learn | Linear Regression | Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
