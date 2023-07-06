import csv

# Function to generate a list of time strings in HH:MM:SS format
def generate_times():
    times = []
    for hour in range(24):
        for minute in range(60):
            time_str = f"{hour:02d}:{minute:02d}:00"
            times.append(time_str)
    return times

# Generate the list of time strings
times = generate_times()

# Define the CSV file path and column headers
csv_file = "kai.csv"
headers = ["Time", "Gallon"]

# Fill the "Gallon" column with zeros
gallons = ['0'] * len(times)

# Write the data to the CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(zip(times, gallons))

print(f"CSV file '{csv_file}' has been created in the current directory.")
