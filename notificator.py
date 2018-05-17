import smtplib


class Notificator:

    def __init__(self, name):
        self.name = name

    def send_email(self, receiver_email, name):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.login("youremailusername", "password")
        msg = "Dear, ", name, " your reservation processed successfully!"
        server.sendmail("sender@gmail.com", receiver_email, msg)

    def reserved_notification(self, table, date):
        print("The table No.", table.number, " is not available fon ", date)

    def available_notification(self, table, date):
        print("The table No.", table.number, " is available for reservation on ", date)
