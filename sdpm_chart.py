# -*- coding: utf-8 -*-
"""SDPM_Chart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mmc1hvX3ytPFdGk1fU4IqPN-9I5fnuTR
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data from an Excel file
df = pd.read_excel('/content/Football_Championship_2023_Shots_With_Expected_Points_JSON.xlsx')

# Ensure the 'Minute' column is numeric
df['Minute'] = pd.to_numeric(df['Minute'], errors='coerce')

# Drop rows where 'Minute' could not be converted to a number
df = df.dropna(subset=['Minute'])

# Convert 'Minute' to integers
df['Minute'] = df['Minute'].astype(int)

# Convert minutes to intervals
df['Time_Interval'] = pd.cut(df['Minute'], bins=range(0, 91, 10), right=False, labels=[f"{i}-{i+10}" for i in range(0, 90, 10)])

# Group by TeamName and Time_Interval, then calculate the mean of Shot_Distance
average_shot_distance = df.groupby(['TeamName', 'Time_Interval'])['Shot_Distance'].mean().unstack(fill_value=0)

# Calculate a common maximum y-axis limit if there are any valid data points
max_distance = average_shot_distance.values.max()
if pd.isna(max_distance):
    max_distance = 80  # default value if all data is NaN

# Plotting and saving separate bar charts for each team
for team, data in average_shot_distance.iterrows():
    data.plot(kind='bar', figsize=(10, 6))
    plt.title(f'Average Shot Distance for {team}')
    plt.xlabel('Time Interval')
    plt.ylabel('Average Shot Distance (meters)')
    plt.xticks(rotation=45)
    plt.ylim(0, max_distance + 5)  # Set a common scale for better comparison
    plt.tight_layout()
    plt.savefig(f'/content/{team}_SDPM_Chart.png')  # Save each chart with the name "{team}_SDPM_Chart.png"
    plt.close()  # Close the current figure to free up memory