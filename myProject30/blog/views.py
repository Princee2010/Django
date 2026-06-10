from django.core.mail import EmailMessage , send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse

# def send_test_email(request):
#     subject = "Welcome to My Blog"
#     message = "Thank you for subscribing to My Blog!"
#     from_email = "princeebhingradiya20@gmail.com"
#     recipient_list = ["24dit006@charusat.edu.in"]

#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse("Test email sent successfully!")

def send_test_email(request):
    subject = "Welcome to My Blog"
    message = render_to_string('email/welcome_email.html', {
        'username': 'Princee',
        'course': 'Django Tutorial',
        })
    email = EmailMessage(
        subject,
        message,
        "princeebhingradiya20@gmail.com",
        ["24dit006@charusat.edu.in"]
    )
    email.content_subtype = "html"  # Main content is now text/html
    email.send()
    return HttpResponse("Test email sent successfully!")