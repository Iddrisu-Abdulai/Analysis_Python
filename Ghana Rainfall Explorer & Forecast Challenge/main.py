import xlrd
import pandas as pd
import random


# File containing rainfall dataset
FILE_NAME = "ghana-precipitation-2000-2015.csv"

# Mapping month numbers to names for display
MONTHS = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

# Number of prediction rounds in the game
NUM_ROUNDS = 10


def main():
    """Main game loop controlling rounds, scoring, and final results."""

    print("🌧 Ghana Rainfall Forecast Challenge\n")

    # Load dataset
    df = load_data()

    score = 0  # Track correct predictions

    # Run multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):

        print(f"\n===== Round {round_num} =====")

        # Play one round and check if user is correct
        if play_round(df):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        print(f"Score: {score}")

    # Final results
    print("\nGame Over")
    print(f"Final Score: {score}/{NUM_ROUNDS}")

    # Calculate accuracy
    accuracy = (score / NUM_ROUNDS) * 100
    print(f"\nForecast Accuracy: {accuracy:.0f}%")

    # Performance ranking system
    if accuracy >= 90:
        print("Weather Master")
    elif accuracy >= 70:
        print("Chief Meteorologist")
    elif accuracy >= 50:
        print("Weather Analyst")
    else:
        print("Junior Forecaster")


def load_data():
    """Loads and cleans rainfall dataset."""

    df = pd.read_csv(FILE_NAME)

    # Keep only needed columns from dataset
    df = df[["Precipitation (mm)", "\tYear", " Month"]]

    # Rename columns for easier access
    df.columns = ["rainfall", "year", "month"]

    return df


def get_category(rainfall):
    """Converts rainfall value into category."""

    if rainfall <= 50:
        return "Low"
    elif rainfall <= 120:
        return "Medium"
    else:
        return "High"


def get_trend(values):
    """Determines rainfall trend from last 3 values."""

    if values[2] > values[1] > values[0]:
        return "Increasing"
    elif values[2] < values[1] < values[0]:
        return "Decreasing"
    else:
        return "Mixed"


def play_round(df):
    """Runs a single prediction round."""

    # Pick random index ensuring we have previous 3 values
    index = random.randint(3, len(df) - 1)

    print("\nPrevious Rainfall Data")
    print("----------------------")

    recent_values = []

    year = int(df.iloc[index]["year"])
    print(f"Year: {year}\n")

    # Show last 3 months of rainfall data
    for i in range(index - 3, index):

        month_num = int(df.iloc[i]["month"])
        month_name = MONTHS[month_num]

        rainfall = round(df.iloc[i]["rainfall"], 1)
        recent_values.append(rainfall)

        print(f"{month_name:<10}: {rainfall} mm")

    # Show trend hint
    trend = get_trend(recent_values)
    print(f"\nForecast Tip: Rainfall trend is {trend}\n")

    # User prediction options
    print("Predict the NEXT month's rainfall")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    choice = input("Your prediction (1-3): ")

    # Validate input
    while choice not in ["1", "2", "3"]:
        choice = input("Please enter 1, 2, or 3: ")

    categories = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    guess = categories[choice]

    # Get actual value
    actual_rainfall = df.iloc[index]["rainfall"]
    actual_category = get_category(actual_rainfall)

    target_month = MONTHS[int(df.iloc[index]["month"])]

    print()
    print(f"Forecast Month: {target_month}")
    print(f"Actual Rainfall: {round(actual_rainfall, 1)} mm")
    print(f"Category: {actual_category}")

    # Compare prediction
    return guess == actual_category


if __name__ == "__main__":
    main()