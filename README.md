# Iris Flower Prediction App

このアプリケーションは、Irisの花の特徴量に基づいてその種類を予測します。事前に学習されたRandomForestモデルを使用した[API](https://github.com/TakumiKishimoto/my_fastapi_app)を用いて、花の種類と予測確率を表示します。[こちら](https://myrandomforestapi.streamlit.app/)から実行できます。

## プロジェクト構成

```
├── app.py               # Streamlitアプリケーションのメインスクリプト
├── pyproject.toml        # Poetryによる依存関係管理ファイル
├── poetry.lock           # Poetryのロックファイル
└── README.md             # このREADMEファイル
```

## インストール手順

1. リポジトリをクローンします。

    ```bash
    git clone <リポジトリURL>
    cd <プロジェクトディレクトリ>
    ```

2. Poetryを使用して依存関係をインストールします。

    ```bash
    poetry install
    ```

3. 仮想環境に入ります。

    ```bash
    poetry shell
    ```

## ローカルでのアプリケーションの使用方法

1. アプリケーションを起動します。

    ```bash
    streamlit run app.py
    ```

2. ブラウザでアプリケーションにアクセスします。デフォルトでは、[http://localhost:8000](http://localhost:8000) で表示されます。

3. 以下のフォームにIrisの特徴量を入力し、「Predict」ボタンをクリックします。

    - Sepal Length (cm)
    - Sepal Width (cm)
    - Petal Length (cm)
    - Petal Width (cm)

4. 予測結果と各クラスの確率が表示されます。予測された花の種類とその確率、特徴量の重要性がグラフで表示されます。

## APIのエンドポイント

アプリケーションは以下のエンドポイントにリクエストを送信して予測を行います。

### `POST/predict/`

Irisの特徴量を入力し、予測を行います。

#### リクエストフォーマット

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

#### レスポンスフォーマット

```json
{
  "prediction": "setosa",
  "prediction_proba": [0.9, 0.05, 0.05],
  "feature_importances": [0.25, 0.1, 0.4, 0.25]
}
```

## モデルについて

このアプリケーションでは、事前に学習されたRandomForestモデルを使用してIrisの花の種類を予測しています。モデルの詳細は、[API](https://github.com/TakumiKishimoto/my_fastapi_app)を参照してください。

