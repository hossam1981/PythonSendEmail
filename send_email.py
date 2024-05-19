import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, to_emails, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    # msg['To'] = to_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

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


if __name__ == "__main__":
    subject = "Test Email"
    body = "This is a  a7777ah email sent from Python."
    # Replace with the recipient's email address
    to_email = ["spiderdash4u@gmail.com", "hossam.elnaggar.ny@gmail.com"]
    from_email = "spiderdash@hotmail.com"  # Replace with your email address
    smtp_server = "smtp.office365.com"  # Yahoo SMTP server
    smtp_port = 587  # Yahoo SMTP port for TLS
    smtp_user = "spiderdash@hotmail.com"  # Your Yahoo email address
    smtp_password = "rivertotheSEA"  # Your Yahoo email password

    send_email(subject, body, to_email, from_email,
               smtp_server, smtp_port, smtp_user, smtp_password)
