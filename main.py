import pandas
import datetime as dt
import smtplib
import random

my_email = "yoursample@gmail.com"
password = "********"               #enable 2-step verification in mail and generate app password code

# CURRENT MONTH AND DAY
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# Email sending function
def send_email(content):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bday_person_email,
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )

# Generate letter content and send email
def generate_letter():
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as txt_file:
        content = txt_file.read()
        # Replace placeholder and reassign to content
        content = content.replace("[NAME]", bday_person_name)
        send_email(content)

# Load data and check for birthdays
original_data = pandas.read_csv("birthdays.csv")
list_of_data = original_data.to_dict(orient="records")

for info in list_of_data:
    birth_month = info["month"]
    birth_day = info["day"]
    if birth_day == current_day and birth_month == current_month:
        bday_person_name = info["name"]
        bday_person_email = info["email"]
        generate_letter()
