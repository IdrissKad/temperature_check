# Temperature check
The goal of this repo is to create an automated tool to monitor temperatures in three differents cities, New York, Paris and London. It contains 2 pythons file.

### Imports and packages

The main packages needed are requests, csv, datetime and pandas.

### Data Importation

The data is imported through the API : https://api.openweathermap.org/data/2.5/forecast. From the API import the current temperatures and the forecasted temperature in the next 3 hours, using update_temperature.py.

### Storing data

The data is stored in an updated csv file, containing the time, the cities, the forecasted temperature and the current temperature.

### Monitoring

Check to see if the forecasted temperature is superior to the temperature it was at the same time. Receiving an alert by email. Using monitor_temperature.py

### Automation

Use a cron job to automate the code every hour.
