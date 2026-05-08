import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("credit_model.pkl", "rb"))

st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.title-box {
    background: linear-gradient(90deg, #1f2937, #334155);
    padding: 30px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
}
.result-safe {
    background-color: #dcfce7;
    color: #166534;
    padding: 20px;
    border-radius: 15px;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
}
.result-risky {
    background-color: #fee2e2;
    color: #991b1b;
    padding: 20px;
    border-radius: 15px;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
    <h1>Credit Risk Prediction System</h1>
    <p>Predict whether a customer is financially safe or risky using credit history.</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([2, 1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Customer Details")

    c1, c2, c3 = st.columns(3)

    with c1:
        LIMIT_BAL = st.number_input("Credit Limit", min_value=0, value=50000)
        SEX = st.selectbox("Gender", ["Male", "Female"])
        EDUCATION = st.selectbox("Education", ["Graduate School", "University", "High School", "Others"])

    with c2:
        MARRIAGE = st.selectbox("Marital Status", ["Married", "Single", "Others"])
        AGE = st.number_input("Age", min_value=18, max_value=100, value=30)
        PAY_0 = st.selectbox("Latest Payment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    with c3:
        PAY_2 = st.selectbox("Payment Status Month 2", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        PAY_3 = st.selectbox("Payment Status Month 3", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        PAY_4 = st.selectbox("Payment Status Month 4", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    st.divider()

    st.subheader("Billing Amounts")
    b1, b2, b3 = st.columns(3)

    with b1:
        BILL_AMT1 = st.number_input("Bill Amount 1", value=20000)
        BILL_AMT2 = st.number_input("Bill Amount 2", value=18000)

    with b2:
        BILL_AMT3 = st.number_input("Bill Amount 3", value=15000)
        BILL_AMT4 = st.number_input("Bill Amount 4", value=12000)

    with b3:
        BILL_AMT5 = st.number_input("Bill Amount 5", value=10000)
        BILL_AMT6 = st.number_input("Bill Amount 6", value=8000)

    st.divider()

    st.subheader("Payment Amounts")
    p1, p2, p3 = st.columns(3)

    with p1:
        PAY_AMT1 = st.number_input("Payment Amount 1", value=5000)
        PAY_AMT2 = st.number_input("Payment Amount 2", value=4000)

    with p2:
        PAY_AMT3 = st.number_input("Payment Amount 3", value=3000)
        PAY_AMT4 = st.number_input("Payment Amount 4", value=2000)

    with p3:
        PAY_AMT5 = st.number_input("Payment Amount 5", value=1500)
        PAY_AMT6 = st.number_input("Payment Amount 6", value=1000)

    PAY_5 = 0
    PAY_6 = 0

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Prediction Panel")
    st.write("Fill customer data and click below.")

    gender_map = {"Male": 1, "Female": 2}
    education_map = {
        "Graduate School": 1,
        "University": 2,
        "High School": 3,
        "Others": 4
    }
    marriage_map = {
        "Married": 1,
        "Single": 2,
        "Others": 3
    }

    if st.button("Predict Credit Risk", use_container_width=True):
        data = np.array([[
            LIMIT_BAL,
            gender_map[SEX],
            education_map[EDUCATION],
            marriage_map[MARRIAGE],
            AGE,
            PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
            BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
            PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6
        ]])

        prediction = model.predict(data)

        if prediction[0] == 0:
            st.markdown('<div class="result-safe">SAFE CUSTOMER ✅</div>', unsafe_allow_html=True)
            st.write("This customer has lower predicted default risk.")
        else:
            st.markdown('<div class="result-risky">RISKY CUSTOMER ❌</div>', unsafe_allow_html=True)
            st.write("This customer has higher predicted default risk.")

    st.info("Note: This is a machine learning prediction, not a final financial decision.")
    st.markdown('</div>', unsafe_allow_html=True)