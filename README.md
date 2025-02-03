# Data Bike Share App

This application is a data analysis project using Streamlit that allows users to explore the Bike Share dataset. Users can filter data by date and view the number of bicycles borrowed in a selected time range.

## Features 🧰
- **Filter Date & Time**: Users can select a date range to view bicycle rental data within a certain period.
- **Visualization**: Displays a graph of the number of bicycles borrowed based on filtered dates.

## Dataset 📊
This app use two dataset:
- `day.csv`: Day based dataset.
- `hour.csv`: Hour based dataset.

## Prerequisites 🛠️

Before running the application, make sure you have Python installed. You can install all the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## How to run app 🏃🏻‍♂️

1. **Clone Repository**: Clone this repository
   ```bash
   git clone https://github.com/desxtra/dataAnalysisPython
   ```

2. **Go into cloned repository**
   ```bash
   cd dataAnalysisPython
   ```

3. **Run the dashboard with streamlit**
   ```bash
   streamlit run dashboard.py
   ```