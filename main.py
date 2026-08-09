from dotenv import load_dotenv
import os
import smtplib
from datetime import datetime
import pandas
import random

load_dotenv()

my_email= os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")

today=datetime.now()
today_tuple=(today.month, today.day)
data= pandas.read_csv("birthday.csv")
data_dict= {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in data_dict:
    birthday_person = data_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        letter_contents= letter_file.read()
        letter_contents=letter_contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
     connection.starttls()
     connection.login(user=my_email, password=password)
     connection.sendmail(

         from_addr=my_email,
         to_addrs=birthday_person["email"],
         msg=f"Subject: happy birthday \n\n{letter_contents}"

     )



