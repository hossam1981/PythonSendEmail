import smtplib  # SMTP protocol to send emails
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


def send_email(subject, body, to_emails, from_email, smtp_server, smtp_port, smtp_user, smtp_password, image_path):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image
    with open(image_path, 'rb') as img:
        img_data = img.read()
    image = MIMEImage(img_data, name=os.path.basename(image_path))
    msg.attach(image)

    try:
        # Connect to the SMTP server
        print("Connecting to the SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()  # Secure the connection
        print("Logging in to the SMTP server...")
        server.login(smtp_user, smtp_password)
        print("Sending the email...")
        server.sendmail(from_email, to_emails, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def schedule_email():
    subject = "Test Email"
    body = "This is a test email sent from Python."
    image_path = "/Users/hossamelnaggar/Dropbox/My_projects/python_proj/python_sendemail/post/post1.png"

    to_emails = ["spiderdash4u@gmail.com", "hossam.elnaggar.ny@gmail.com"]
    from_email = "spiderdash@hotmail.com"
    smtp_server = "smtp.office365.com"  # SMTP server for Hotmail/Outlook
    smtp_port = 587  # SMTP port for TLS
    smtp_user = os.getenv('SMTP_USER')  # your email on .env file
    smtp_password = os.getenv('SMTP_PASSWORD')  # ur pass on .env

    send_email(subject, body, to_emails, from_email, smtp_server,
               smtp_port, smtp_user, smtp_password, image_path)


if __name__ == "__main__":
    # Schedule the job
    schedule.every().day.at("08:00").do(schedule_email)  # Adjust the time as needed

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)


# 1- Activate the Virtual Environment
#   source email_project_env/bin/activate
# 2- run the script
#   python3 main.py
