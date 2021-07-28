4
import smtplib, ssl
 
def smail():
  port = 587 
  smtp_server = "smtp.gmail.com"
 
  receiver_email = input("Enter Email id you want to send wishes: ")

  sender_email = input("Enter your email ID: ")

  password = input("Type your password and press enter: ")
 
  message = """\
  Subject: Hi Friend
  Life is a journey. Don’t imprison yourself in a rut. Break free and travel. Wander as if you’re lost. It’s the only way to discover yourself. Bon voyage Have a safe and memorable trip. Lets meet after your trip ends so that you can share your memories and your trip experience with us
  Bye!
  """
  #here is the message which will be sent
  context = ssl.create_default_context()
  with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo() 
      server.starttls(context=context)
      server.ehlo()  
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)