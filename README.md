# Temperature Monitoring
This repository contains two Python scripts designed to update and monitor temperature data for various cities. Below are descriptions and instructions for each script.

## Scripts

### 1. update_temperature.py

Purpose: This script fetches the current temperature for specified cities and stores the data in a local CSV file.

Features:

- Fetches temperature data using the OpenWeatherMap API : https://api.openweathermap.org/data/2.5/forecast.
- Stores temperatures along with timestamps in a CSV file.

### 2. monitor_temperature.py

Purpose: This script monitors the temperature data stored by update_temperature.py and checks for deviations between the forecasted temperatures (for the next three hours) and actual temperatures. If the deviation exceeds a specified threshold (1°C), it sends an email notification.

Features:

- Compares forecasted and actual temperatures from a CSV file.
- Sends email alerts if temperature deviations exceed a predefined threshold.

## Requirements

To run these scripts, you will need:

- Python 3.6 or higher.
- requests library for making API calls.
- smtplib and email.message for sending emails.


### Automation

Use a cron job to automate the code every hour. Or run the codes update_temperature.py and monitor_temperature.py every hour.
