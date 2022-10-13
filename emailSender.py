
import smtplib, ssl
import datetime

class MailSender:

    def mailSenderInformation(mailContent,Information):


        SMTP_SERVER = "smtp.gmail.com"
        PORT = 587  # For starttls
        EMAIL = "rgoksoy13@gmail.com"
        PASSWORD = "tctautwpghqacaqt"
        Gönderilecek_Mail_Adresi="ramazangoksoy@gmail.com"

        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(EMAIL, PASSWORD)
            
            user=mailContent.first_name
            mail=mailContent.email
            timeLogin=str(datetime.datetime.now()).split(".")[0]
            if(Information=="Login"):
                body=f"{user} adli kullaci kisisi, {mail} email adresi ile sisteme GIRIS yapti ..\n\n Time: {timeLogin}"
            elif(Information=="Logout"):
                body=f"{user} adli kullaci kisisi, {mail} email adresi ile sistemden CIKIS yapti ..\n\n Time: {timeLogin}"   
                
            elif(Information=="SingUp"):
                body=f"{user} adli kullaci kisisi, {mail} email adresi ile sisteme YENI KAYIT YAPTIRDI yapti ..\n\n Time: {timeLogin}"   
            else:
                body="Nothing"
                print("Nothing")
                
            subject="SYSTEM INFORMATION WEBSITE"
            message= f"{subject}\n\n{(body)}".encode('utf-8').strip()

            server.sendmail(EMAIL, Gönderilecek_Mail_Adresi, message)





# user={"user":"Ramazan","mail":"ramazangoksoy@gmail.com"}   
# mailSenderInformation(user) 






