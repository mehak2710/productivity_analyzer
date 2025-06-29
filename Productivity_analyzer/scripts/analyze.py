import pandas as pd

filename = "../data/log.csv"
df = pd.read_csv(filename)

# Show column names
print("📋 Columns in CSV:", df.columns.tolist())

# Validate required columns
required = ['work_hours', 'sleep_hours', 'mood']
missing = [col for col in required if col not in df.columns]

if missing:
    print(f"\n⚠️ Missing columns: {', '.join(missing)}")
    print("Please ensure the CSV has this header: date,work_hours,sleep_hours,mood")
else:
    df['work_hours'] = pd.to_numeric(df['work_hours'], errors='coerce')
    df['sleep_hours'] = pd.to_numeric(df['sleep_hours'], errors='coerce')

    print("\n📊 Productivity Summary:")
    print(f"• Average Work Hours: {df['work_hours'].mean():.2f}")
    print(f"• Average Sleep Hours: {df['sleep_hours'].mean():.2f}")

    print("\n😄 Mood Count:")
    print(df['mood'].value_counts())
