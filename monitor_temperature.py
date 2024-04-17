import csv
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage

# Constants
CSV_FILE = 'weather_data.csv'
EMAIL_SENDER = 'codetemperature2024@outlook.com'
EMAIL_PASSWORD = 'Temperature2024'
EMAIL_RECEIVER = 'codetemperature2024@outlook.com'
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587 
TEMP_DEVIATION_THRESHOLD = 1

def send_email(city, forecast_time, current_temp, forecast_temp):
    message = EmailMessage()
    message.set_content(f"In {city}, the temperature forecasted at {forecast_time} was {forecast_temp}°C, which deviates by more than 1°C from the current temperature of {current_temp}°C.")
    message['Subject'] = f"Temperature Deviation Alert in {city}"
    message['From'] = EMAIL_SENDER
    message['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()  
            server.starttls() 
            server.ehlo()  
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(message)
            print("Email sent successfully!") 
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_temperature_deviations():
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    for i in range(10, len(data)):
        current_city = data[i][0]
        current_time = data[i][1]
        current_temp = float(data[i][2])
        forecast_temp = float(data[i-9][3])

        if abs(current_temp - forecast_temp) > TEMP_DEVIATION_THRESHOLD:
            send_email(current_city, data[i-9][1], current_temp, forecast_temp)

if __name__ == "__main__":
    check_temperature_deviations()
