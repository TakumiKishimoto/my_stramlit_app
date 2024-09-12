import streamlit as st
import requests
import pandas as pd
import altair as alt

API_URL = st.secrets["API_URL"]
# API_URL = "http://localhost:8000"

# タイトル
st.title("Iris Flower Prediction")

# 初期値を設定
default_sepal_length = 5.1
default_sepal_width = 3.5
default_petal_length = 1.4
default_petal_width = 2.0

# 入力フォーム
st.header("Input the features of the Iris flower")

sepal_length = st.number_input("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=default_sepal_length, format="%.1f", step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=2.0, max_value=5.0, value=default_sepal_width, format="%.1f", step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=1.0, max_value=7.0, value=default_petal_length, format="%.1f", step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=2.5, value=default_petal_width, format="%.1f", step=0.1)

# 推論ボタン
if st.button("Predict"):
    # 入力データをAPIに送信
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    response = requests.post(f"{API_URL}/predict/", json=payload)

    if response.status_code == 200:
        result = response.json()
        prediction = result["prediction"]
        prediction_proba = result["prediction_proba"]
        # rename prediction_proba keys 0, 1, 2 to setosa, versicolor, virginica
        prediction_proba = {"setosa": prediction_proba[0], "versicolor": prediction_proba[1], "virginica": prediction_proba[2]}
        feature_importances = result["feature_importances"]

        st.success(f"The predicted class is: {prediction}")

        # Create a DataFrame for the prediction probabilities
        proba_df = pd.DataFrame(list(prediction_proba.items()), columns=["Class", "Probability"])

        # Create an Altair chart with rotated labels
        chart = alt.Chart(proba_df).mark_bar().encode(
            x=alt.X('Class:N', sort=None, axis=alt.Axis(labelAngle=45)),  # Rotate x-axis labels
            y='Probability:Q',
            color='Class:N'
        ).properties(
            title="Prediction Probability"
        )

        st.altair_chart(chart, use_container_width=True)

        # Display feature importances
        col1, col2 = st.columns(2)

        with col1:
            st.write("Feature Importances")
            feature_importances_df = pd.DataFrame({
                "Feature": ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
                "Importance": feature_importances
            })
            st.dataframe(feature_importances_df)

    else:
        st.error("Failed to get prediction")
