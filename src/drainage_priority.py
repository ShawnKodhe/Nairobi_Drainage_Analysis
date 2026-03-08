import pandas as pd
from src.flood_risk import calculate_flood_risk

def calculate_drainage_priority():
    drains = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Nairobi_Drainage\data\drainage.csv")
    flood_risk = calculate_flood_risk()[["neighborhood", "flood_risk_score"]]

    df = drains.merge(flood_risk, on="neighborhood", how="left")

    df["priority_score"] = (
        0.5 * df["blockage_score"] +
        0.3 * df["flood_risk_score"] / df["flood_risk_score"].max() +
        0.2 * df["length_m"] / df["length_m"].max()
    )

    return df.sort_values("priority_score", ascending=False)