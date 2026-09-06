from django.core.mail import send_mail


def send_welcome_email(user):
    send_mail(
        subject="Welcome!",
        message="Your account has been created successfully.",
        from_email=None,
        recipient_list=[user.email],
        fail_silently=False,
    )