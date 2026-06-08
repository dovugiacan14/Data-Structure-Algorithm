import pandas as pd
from collections import deque, Counter



def rising_temperature(weather: pd.DataFrame):
    if weather.empty:
        return pd.DataFrame(columns=["id"])

    prev_day = weather.copy()
    prev_day["recordDate"] = prev_day["recordDate"] + pd.Timedelta(days=1)
    prev_day = prev_day.rename(columns={"temperature": "prev_temp", "id": "prev_id"})

    merged = weather.merge(prev_day, on="recordDate")
    result = merged[merged["temperature"] > merged["prev_temp"]][["id"]]
    return result.reset_index(drop=True)


data = {
    "id": [1, 2, 3, 4, 5, 6, 7],
    "recordDate": [
        "2023-01-01",
        "2023-01-02",
        "2023-01-03",
        "2023-01-04",
        "2023-01-05",
        "2023-01-06",
        "2023-01-07",
    ],
    "temperature": [10, 15, 14, 20, 20, 19, 25],
}

df = pd.DataFrame(data)
df["recordDate"] = pd.to_datetime(df["recordDate"])
print(rising_temperature(df))
