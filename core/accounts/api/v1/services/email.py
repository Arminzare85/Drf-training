from django.core.mail import send_mail


# def send_welcome_email(user , verification_url):
#     send_mail(
#         subject="Welcome!",
#         message=f"""
#         Welcome!

#         Please verify your account using this link:

#         {verification_url}
#         """,
#         from_email=None,
#         recipient_list=[user.email],
#         fail_silently=False,
#     )

def send_verification_email(user , verification_url):
    send_mail(
        subject="Verify your email",
        message=f"""
        Please verify your email using this link:

        {verification_url}
        """,
        from_email=None,
        recipient_list=[user.email],
        fail_silently=False,
    )