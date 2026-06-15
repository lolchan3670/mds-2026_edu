from pathlib import Path
import pickle
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_model(filename: str, model_name: str, model_type: str, train_size: float):

    path = Path("data") / filename
    df = pd.read_csv(path)

    target = df.columns[-1]
    X = pd.get_dummies(df.drop(columns=[target]), drop_first=True)
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=42
     )

    if model_type == "logistic":
        model = LogisticRegression(max_iter=1000)

    elif model_type == "random_forest":
        model = RandomForestClassifier(n_estimators=100, random_state=69)

    elif model_type == "tree":
        model = DecisionTreeClassifier()

    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)

    Path("models").mkdir(exist_ok=True)

    model_path = Path("models") / f"{model_name}.pkl"

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    conn = sqlite3.connect("models.db")

    conn.execute(
        "INSERT INTO training_results (model_name, model_type, accuracy, model_path) VALUES (?, ?, ?, ?)",
        (model_name, model_type, acc, str(model_path))
    )
    conn.commit()
    conn.close()

    return {"accuracy": acc, "model_path": str(model_path)}