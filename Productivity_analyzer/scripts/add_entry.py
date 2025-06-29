import csv
import os
from datetime import date

filename = "../data/log.csv"

# Create log.csv with headers if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "work_hours", "sleep_hours", "mood"])

# Get today's entry
today = str(date.today())
work = input("Hours worked today: ")
sleep = input("Hours slept: ")
mood = input("Mood (Happy/Sad/Neutral): ")

# Save the entry
with open(filename, "a", newline="") as file:
    csv.writer(file).writerow([today, work, sleep, mood])

print("✅ Entry saved successfully!")
