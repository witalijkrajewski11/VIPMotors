from main.abstract_email_sender import AbstractEmailSender
from django.conf import settings


class UserConfirmationEmailSender(AbstractEmailSender):
    template_name = 'profile/confirmation_link'
    subject = "Please verify your account for VIPMotors"
    always_send = True

    @staticmethod
    def example_context():
        data = {
            "activation_key": 'activation_key',
            "expiration_days": settings.ACCOUNT_ACTIVATION_DAYS,
        }
        return data

    def get_context(self):
        context = super().get_context()
        return context
