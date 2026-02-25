🌊 Sea Level Predictor
📌 Project Overview

The Sea Level Predictor analyzes historical global sea level data and uses linear regression to predict future sea level rise through the year 2050.

This project is part of the freeCodeCamp Data Analysis with Python Certification and demonstrates data visualization, statistical modeling, and trend prediction using Python.

📊 Objective

Using historical sea level data from 1880 to 2014, this project:

Visualizes global average sea level changes

Calculates a line of best fit using all available data

Calculates a second line of best fit using data from 2000 onward

Predicts sea level rise through 2050 based on historical trends

📂 Dataset Information

Source:
US Environmental Protection Agency (EPA)
Data from CSIRO (2015) and NOAA (2015)

File Used:
epa-sea-level.csv

Key Columns:
Column Name	Description
Year	Year of recorded data
CSIRO Adjusted Sea Level	Sea level measurement in inches
Lower Error Bound	Lower confidence interval
Upper Error Bound	Upper confidence interval
NOAA Adjusted Sea Level	NOAA-adjusted measurement
📈 Visualizations Generated
1️⃣ Scatter Plot

Displays historical sea level data points from 1880 onward.

2️⃣ First Line of Best Fit

Uses all available data (1880–2014)

Extended to 2050

Predicts long-term trend

3️⃣ Second Line of Best Fit

Uses data from 2000 onward

Extended to 2050

Predicts modern acceleration trend

🛠 Technologies Used

Python 3

Pandas

Matplotlib

SciPy (linregress)


▶ How to Run Locally

1️⃣ Clone Repository

git clone https://github.com/Lucifer-cell-metrix/sea-level-predictor.git

cd sea-level-predictor

2️⃣ Install Dependencies

pip install pandas matplotlib scipy

3️⃣ Run Project

python main.py

The program will generate:

sea_level_plot.png

📊 What This Project Demonstrates

✔ Time series data analysis

✔ Data visualization best practices

✔ Linear regression modeling

✔ Future prediction using historical trends

✔ Clean project structure

✔ Git workflow

📷 Output Example

The generated plot includes:

Scatter plot of sea level data

Red regression line (1880–2050)

Green regression line (2000–2050)

Proper axis labels and title
