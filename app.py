import streamlit as st
import requests
import pandas as pd
from io import StringIO

# RenderにデプロイされたFastAPIのURL
API_URL = "https://my-fastapi-app-helk.onrender.com"

# ファイルアップロードのセクション
st.title("CSV Upload and Retrieve")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # ファイルをFastAPI APIにアップロード
    response = requests.post(
        f"{API_URL}/upload-csv/",
        files={"file": uploaded_file}
    )

    if response.status_code == 200:
        st.success("File uploaded successfully")
    else:
        st.error("Failed to upload file")

    # ファイル名を取得
    file_name = uploaded_file.name

    # CSVファイルをFastAPI APIから取得
    response = requests.get(f"{API_URL}/get-csv/{file_name}")

    if response.status_code == 200:
        # CSVの内容を表示
        data = response.json()
        df = pd.DataFrame(data)
        st.write(df)
    else:
        st.error("Failed to retrieve file")
