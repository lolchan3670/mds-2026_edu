import requests
import streamlit as st

st.title("Train")

with st.form("train_form"):
    filename = st.text_input("Файл данных в data/")
    model_name = st.text_input("Название модели")
    model_type = st.selectbox("Модель", ["logistic", "random_forest"])
    train_size = st.number_input("Размер обучающей выборки", 0.1, 0.9, 0.8, 0.1)
    submit = st.form_submit_button("Обучить модель")

if submit:
    endpoint = (
        "train/logistic"
        if model_type == "logistic"
        else "train/random_forest"
    )
    r = requests.post(
        f"http://localhost:8000/{endpoint}",
        json={
            "filename": filename,
            "model_name": model_name,
            "train_size": train_size
        },
    )
    st.write(r.json())