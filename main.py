import json
import sys
from datetime import datetime, timedelta

def calculate_night_thirds(maghrib_time: str, fajr_time: str):
    maghrib = datetime.strptime(maghrib_time, "%H:%M")
    fajr = datetime.strptime(fajr_time, "%H:%M")

    if fajr <= maghrib:
        fajr += timedelta(days=1)

    night_duration = fajr - maghrib
    third = night_duration / 3

    first_third = maghrib + third
    second_third = maghrib + (2 * third)
    last_third = fajr - third

    return {
        "first_third_ends": first_third.time().strftime("%H:%M"),
        "second_third_ends": second_third.time().strftime("%H:%M"),
        "last_third_starts": last_third.time().strftime("%H:%M"),
        "fajr": fajr.time().strftime("%H:%M")
    }

if __name__ == "__main__":
    # قراءة input.json من Apify
    with open("INPUT.json", "r") as f:
        data = json.load(f)

    maghrib_time = data.get("maghrib", "18:43")
    fajr_time = data.get("fajr", "04:00")

    results = calculate_night_thirds(maghrib_time, fajr_time)

    # إخراج النتائج في output.json
    with open("OUTPUT.json", "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
