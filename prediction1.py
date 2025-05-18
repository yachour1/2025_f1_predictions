import fastf1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

# Enable FastF1 caching
fastf1.Cache.enable_cache("f1_cache")

# Load multiple FastF1 2024 race sessions
sessions_2024 = []
race_numbers = [1, 2, 3, 4, 5, 6]  # Bahrain, Saudi Arabia, Australia, Japan, China
for race_num in race_numbers:
    try:
        session = fastf1.get_session(2025, race_num, "R")
        session.load()
        sessions_2024.append(session)
        print(f"✅ Loaded session for race {race_num}")
    except Exception as e:
        print(f"⚠️ Could not load session for race {race_num}: {str(e)}")

# Extract lap times from all sessions
all_laps = pd.DataFrame()
for session in sessions_2024:
    laps = session.laps[["Driver", "LapTime"]].copy()
    laps.dropna(subset=["LapTime"], inplace=True)
    laps["LapTime (s)"] = laps["LapTime"].dt.total_seconds()
    all_laps = pd.concat([all_laps, laps])

# Calculate average lap time per driver
driver_avg_laptimes = all_laps.groupby("Driver")["LapTime (s)"].mean().reset_index()

# 2025 Qualifying Data (meilleur tour en secondes, Q1–Q3)
qualifying_2025 = pd.DataFrame({
    "Driver": [
        "Oscar Piastri", "Max Verstappen", "George Russell", "Lando Norris",
        "Fernando Alonso", "Carlos Sainz", "Alexander Albon", "Lance Stroll",
        "Isack Hadjar", "Pierre Gasly", "Charles Leclerc", "Lewis Hamilton",
        "Kimi Antonelli", "Gabriel Bortoleto", "Franco Colapinto",
        "Liam Lawson", "Nico Hulkenberg", "Esteban Ocon", "Oliver Bearman",
        "Yuki Tsunoda"
    ],
    "QualifyingTime (s)": [
        74.670, 74.704, 74.807, 74.962, 75.431, 75.198,
        75.473, 75.497, 75.510, 75.505, 75.604, 75.765,
        75.772, 76.260, 76.256, 76.379, 76.518, 76.613,
        76.918,    None   # DNF → pas de temps
    ]
})

# Map full names to FastF1 3-letter codes
driver_mapping = {
    "Oscar Piastri":     "PIA", "Max Verstappen":   "VER",
    "George Russell":    "RUS", "Lando Norris":     "NOR",
    "Fernando Alonso":   "ALO", "Carlos Sainz":     "SAI",
    "Alexander Albon":   "ALB", "Lance Stroll":     "STR",
    "Isack Hadjar":      "HAD", "Pierre Gasly":     "GAS",
    "Charles Leclerc":   "LEC", "Lewis Hamilton":   "HAM",
    "Kimi Antonelli":    "ANT", "Gabriel Bortoleto": "BOR",
    "Franco Colapinto":  "COL", "Liam Lawson":      "LAW",
    "Nico Hulkenberg":   "HUL", "Esteban Ocon":      "OCO",
    "Oliver Bearman":    "BEA", "Yuki Tsunoda":      "TSU"
}

qualifying_2025["DriverCode"] = qualifying_2025["Driver"].map(driver_mapping)

# Drop rows with missing qualifying times
qualifying_2025 = qualifying_2025.dropna(subset=["QualifyingTime (s)"])

# Merge 2025 Qualifying Data with 2024 Race Data
merged_data = qualifying_2025.merge(driver_avg_laptimes, left_on="DriverCode", right_on="Driver", how="left", suffixes=('', '_historical'))

# Fill missing historical lap times with the mean of all drivers
mean_lap_time = driver_avg_laptimes["LapTime (s)"].mean()
merged_data["LapTime (s)"] = merged_data["LapTime (s)"].fillna(mean_lap_time)

# Calculate weighted scores (70% qualifying, 30% historical performance)
merged_data["WeightedScore"] = (
    0.7 * merged_data["QualifyingTime (s)"] + 
    0.3 * merged_data["LapTime (s)"]
)

# Use weighted score as feature
X = merged_data[["WeightedScore"]]
y = merged_data["LapTime (s)"]

if X.shape[0] == 0:
    raise ValueError("Dataset is empty after preprocessing. Check data sources!")

# Train Gradient Boosting Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=39)
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=39)
model.fit(X_train, y_train)

# Calculate weighted scores for 2025 qualifying
qualifying_2025 = qualifying_2025.merge(driver_avg_laptimes, left_on="DriverCode", right_on="Driver", how="left", suffixes=('', '_historical'))
qualifying_2025["LapTime (s)"] = qualifying_2025["LapTime (s)"].fillna(mean_lap_time)

qualifying_2025["WeightedScore"] = (
    0.7 * qualifying_2025["QualifyingTime (s)"] + 
    0.3 * qualifying_2025["LapTime (s)"]
)

# Predict using weighted scores
predicted_lap_times = model.predict(qualifying_2025[["WeightedScore"]])
qualifying_2025["PredictedRaceTime (s)"] = predicted_lap_times

# Rank drivers by predicted race time
qualifying_2025 = qualifying_2025.sort_values(by="PredictedRaceTime (s)")

# Replace specific driver names
qualifying_2025.loc[qualifying_2025.index[0], "Driver"] = "Schoura Kouki"  # Premier
qualifying_2025.loc[qualifying_2025.index[-2], "Driver"] = "Sarra Kouki"   # Avant-dernier
qualifying_2025.loc[qualifying_2025.index[-1], "Driver"] = "Yasmine Achour"  # Dernier

# Print final predictions
print("\n🏁 Predicted 2025 Emilia-Romagna GP Winner 🏁\n")
print(qualifying_2025[["Driver", "PredictedRaceTime (s)", "QualifyingTime (s)"]].to_string())

# Evaluate Model
y_pred = model.predict(X_test)
print(f"\n🔍 Model Error (MAE): {mean_absolute_error(y_test, y_pred):.2f} seconds")
print("\nNote: Predictions are weighted 70% qualifying performance, 30% historical performance")
