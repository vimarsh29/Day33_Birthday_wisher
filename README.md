# 🎂 Automated Python Birthday Wisher

An automated Python script that reads user details from a CSV file, checks for matching birth dates and months against the current day, and automatically sends personalized birthday greeting emails using SMTP.

## 🚀 Features

*   **CSV Parsing:** Reads recipient data dynamically from a simple CSV spreadsheet.
*   **Date Matching:** Automatically matches the current day and month while ignoring the birth year.
*   **Secure Emailing:** Uses `smtplib` with TLS encryption to securely send emails.
*   **Error Handling:** Skips malformed dates without crashing and logs status outputs to the console.

## 📂 Project Structure

```text
├── birthday_wisher.py     # Main Python script
├── birthdays.csv          # Recipient contact and birthday database
└── README.md              # Project documentation
```

## 🛠️ Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.x installed on your machine. This project relies entirely on Python built-in standard libraries (`csv`, `datetime`, `smtplib`), so no external packages are required.

### 2. Configure the Database
Create a file named `birthday.csv` in the root directory. Populate it using the `YYYY-MM-DD` date format:

```csv
name,email,birth_date
Alice Smith,alice@example.com,1995-08-07
Bob Jones,bob@example.com,1990-11-23
```

### 3. Configure Email Credentials
Open `main.py` and update the configuration variables at the top of the file:

```python
SMTP_SERVER = "://gmail.com"  # Replace with your email provider's SMTP server
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Do NOT use your primary password
```

> ⚠️ **Security Note for Gmail Users:** You must enable **2-Step Verification** on your Google Account and generate an **App Password** to use as your `SENDER_PASSWORD`. Regular passwords will be blocked by Google.
Dont hardcode your credentials in the script. Instead, consider using environment variables or a secure configuration file.
## 💻 Usage

Run the script manually using your terminal:

```bash
python main.py
```

## ⏰ Automation (Optional)

To run this script automatically every day, you can set up a background scheduler:

*   **Windows:** Use **Task Scheduler** to trigger `main.py` daily.
*   **Mac/Linux:** Add a **Cron Job** by running `crontab -e` and inserting the following line to execute it daily at 9:00 AM:
    ```text
    0 9 * * * /usr/bin/python3 /path/to/your/birthday_wisher.py
    ```

## 📄 License
This project is open-source and available under the MIT License.