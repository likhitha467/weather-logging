
import csv
import time
from datetime import datetime
import os

# CSV file name
filename = "WEATHER_DATA.csv"

# Create CSV file and headings
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Date",
            "Time",
            "DS1621_Temperature",
            "DHT11_Temperature",
            "Humidity"
        ])

print("ENVIRONMENTAL DATA LOGGER")
print("-------------------------")

try:
    while True:

        # Enter simulated sensor readings
        ds_temp = float(input("Enter DS1621 temperature: "))
        dht_temp = float(input("Enter DHT11 temperature: "))
        humidity = float(input("Enter humidity: "))

        # Get date and time
        now = datetime.now()

        date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        # Store readings in CSV
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                date,
                current_time,
                ds_temp,
                dht_temp,
                humidity
            ])

        print("Data saved successfully!")
        print("-------------------------")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nData logging stopped.")
    print("CSV file saved:", filename)

import csv
import tkinter as tk

# Read CSV data
dates = []
ds_temp = []
dht_temp = []
humidity = []

with open("WEATHER_DATA.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["Time"])
        ds_temp.append(float(row["DS1621_Temperature"]))
        dht_temp.append(float(row["DHT11_Temperature"]))
        humidity.append(float(row["Humidity"]))

if not dates:
    print("No data available in CSV file.")
    raise SystemExit

# Create graph window
root = tk.Tk()
root.title("Environmental Data Monitoring")
root.geometry("950x700")

def draw_graph(canvas, values, title, unit):
    canvas.create_text(400, 20, text=title,
                       font=("Arial", 14, "bold"))

    left = 65
    right = 750
    top = 55
    bottom = 260

    minimum = min(values)
    maximum = max(values)

    if minimum == maximum:
        minimum -= 1
        maximum += 1

    # Draw axes
    canvas.create_line(left, top, left, bottom)
    canvas.create_line(left, bottom, right, bottom)

    # Draw values
    points = []

    for i, value in enumerate(values):
        x = left + i * (right-left) / max(len(values)-1, 1)
        y = bottom - (value-minimum) * (bottom-top) / (maximum-minimum)
        points.extend([x, y])

        canvas.create_text(left-30, y, text=str(value),
                           font=("Arial", 8))

    # Draw line
    if len(values) > 1:
        canvas.create_line(*points, fill="blue", width=2)

    canvas.create_text(400, 285,
                       text="Recorded readings",
                       font=("Arial", 9))

    canvas.create_text(20, 150, text=unit,
                       angle=90, font=("Arial", 9))

# Temperature graph
canvas1 = tk.Canvas(root, width=850, height=300,
                    bg="white")
canvas1.pack(pady=10)

draw_graph(canvas1, ds_temp,
           "DS1621 Temperature", "Temperature (C)")

# Humidity graph
canvas2 = tk.Canvas(root, width=850, height=300,
                    bg="white")
canvas2.pack(pady=10)

draw_graph(canvas2, humidity,
           "DHT11 Humidity", "Humidity (%)")

root.mainloop()
