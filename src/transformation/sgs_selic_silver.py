import os
import json
from datetime import datetime

import pandas as pd


LANDING_DIR = "data/landing"
SILVER_DIR = "data/silver"


def load_landing_files() -> pd.DataFrame:
    records = []

    for fname in os.listdir(LANDING_DIR):
        if not fname.startswith("sgs_selic_") or not fname.endswith(".json"):
            continue

        path = os.path.join(LANDING_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for row in data:
            row["arquivo_origem"] = fname
            records.append(row)

    df = pd.DataFrame(records)
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
    df["valor"] = pd.to_numeric(df["valor"].str.replace(",", "."), errors="coerce")
    df = df.sort_values("data").reset_index(drop=True)
    return df


def save_to_silver(df: pd.DataFrame) -> str:
    os.makedirs(SILVER_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(SILVER_DIR, f"sgs_selic_silver_{timestamp}.csv")
    df.to_csv(path, index=False)
    return path


def main():
    df_raw = load_landing_files()
    df_silver = transform(df_raw)
    output_path = save_to_silver(df_silver)
    print(f"Arquivo silver salvo em: {output_path}")


if __name__ == "__main__":
    main()
