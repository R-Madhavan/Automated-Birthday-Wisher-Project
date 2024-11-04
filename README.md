#Automated Birthday Wisher Project

A simple Python script that sends birthday wishes via email to friends and family using pre-defined letter templates. The script checks a CSV file for birthdays and sends an email on the corresponding date.

## Features

- Reads birthday information from a CSV file.
- Sends personalized birthday emails.
- Utilizes letter templates for a unique message.

## Requirements

- Python 3.x
- Pandas library for reading CSV files
- Access to a Gmail account for sending emails

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Automated-Birthday-Wisher-Project.git
   cd Automated-Birthday-Wisher-Project
   ```

2. Install the required packages:
   ```bash
   pip install pandas
   ```

3. Create a directory named `letter_templates` and add your letter templates (e.g., `letter_1.txt`, `letter_2.txt`, `letter_3.txt`).

4. Create a `birthdays.csv` file with the following structure:
   ```csv
    name,email,year,month,day
    Brother,sample1@yahoo.com,2000,11,23
    Dad,sample4@gmail.com,1976,10,3
    Mom,sample5@gmail.com,1978,7,5
    Sister,sample2@gmail.com,1999,12,12
   ```

## Usage

1. Update the `my_email` and `password` variables in the script with your email credentials.
2. Run the script:
   ```bash
   main.py
   ```

3. Optionally, set up a task scheduler to run the script daily.

## Note
- Ensure that your email account settings allow sending emails from external apps.
- For Gmail users, you may need to enable "Less secure app access" or generate an App Password.
