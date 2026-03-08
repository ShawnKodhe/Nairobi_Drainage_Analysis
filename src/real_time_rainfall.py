import requests
import pandas as pd

# Nairobi coordinates
NAIROBI_LAT = -1.286389
NAIROBI_LON = 36.817223

API_KEY = "b76fbaab4f22a3e9dc399f5f5f501d4d"  # Replace with your OpenWeatherMap API key

def fetch_real_time_rainfall():
    """
    Fetches current rainfall in Nairobi using OpenWeatherMap API.
    Returns a dataframe similar to rainfall.csv
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={NAIROBI_LAT}&lon={NAIROBI_LON}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Rain volume in last 1 hour (mm)
        rainfall_mm = data.get("rain", {}).get("1h", 0)

        df = pd.DataFrame([{
            "date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            "neighborhood": "Nairobi",
            "rainfall_mm": rainfall_mm
        }])
        return df

    except Exception as e:
        print("Error fetching rainfall:", e)
        return pd.DataFrame([{"date": pd.Timestamp.now(), "neighborhood": "Nairobi", "rainfall_mm": 0}])