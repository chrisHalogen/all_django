from django.shortcuts import render, HttpResponse
import smtplib, ssl

# Create your views here.

def home(request):
    return render(request, 'misc/index.html')

def sendEmail(request):
    # print(request.POST)
    senders_email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email =   # Enter your address
    receiver_email =   # Enter receiver address
    password = 'lekdfrxmbkptuyfm'
    message = f"""\
    Subject: Coming from Portfolio - {subject}

    {message}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    

    return HttpResponse('Email Sent Successfully')

