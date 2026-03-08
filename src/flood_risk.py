import pandas as pd

def calculate_flood_risk():
    rainfall = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Nairobi_Drainage\data\rainfall.csv")
    flood_reports = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Nairobi_Drainage\data\flood_reports.csv")
    neighborhoods = pd.read_csv(r"E:\PYCHARM\PycharmProjects\Nairobi_Drainage\data\neighborhoods.csv")

    # merge datasets
    df = neighborhoods.merge(rainfall.groupby("neighborhood")["rainfall_mm"].mean().reset_index(),
                             on="neighborhood", how="left")
    df = df.merge(flood_reports, on="neighborhood", how="left")

    df["population_density"] = df["population"] / df["area_km2"]

    df["flood_risk_score"] = (
        0.4 * df["rainfall_mm"] +
        0.3 * (df.get("blockage_score", 0) * 10) +  # default 0 if missing
        0.2 * df["flood_count"] +
        0.1 * df["population_density"] / 1000
    )

    return df.sort_values("flood_risk_score", ascending=False)