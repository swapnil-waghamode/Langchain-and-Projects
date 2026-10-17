import smtplib
from email.message import EmailMessage
from langchain.tools import tool

import os
from dotenv import load_dotenv
load_dotenv()

# email details

sender = os.getenv("SENDER_EMAIL")
password  = os.getenv("PASSWORD")       # Password must be an app pasword

def send_email_with_gmail(to:str, subject:str, text_body:str):

  # setting up EmailMessage object

  msg = EmailMessage()

  msg["from"] = sender
  msg["to"] = to
  msg["subject"] = subject
  msg.set_content(text_body)

  # Connect to smtp server and send an email

  try:
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
    
        # login to your account
        server.login(sender, password)
        
        # sending email
        server.send_message(msg)
       

  except Exception as e:
     print(f"An error occurred {e}")


# Creating our email tool

@tool
def send_email(to:str, subject:str, body:str):
   """Send email to any email address by providing the correct email address, subject and body
   Args:
      to - email address
      subject - email subject in one line
      body - email body in plain text
   
   """
   send_email_with_gmail(to, subject, body)

   return "Email sent successfully!"

ALL_TOOLS = [send_email]