import os

from backend.celery_tasks import app
from main.utils import clean_name_for_email
from django.db.models import Model, QuerySet
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.apps import apps

from main import models, constants


@app.task
def send(template_name, context, subject, to):
    context = deserialize_context(context)
    email_html_message = render_to_string(f'main/emails/{template_name}.html', context)
    email_plaintext_message = render_to_string(f'main/emails/{template_name}.txt', context)

    message = EmailMultiAlternatives(
        subject=subject.replace('\n', ''),
        body=email_plaintext_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to]
    )

    message.attach_alternative(email_html_message, 'text/html')
    message.send()


def _get_deserialized_instance_of_model(value: dict):
    if isinstance(value, dict) and value.get('app') and value.get('model') and value.get('pk'):
        model = apps.get_model(value.get('app'), value['model'])
        return model.objects.get(pk=value['pk'])
    else:
        return value


def deserialize_context(serializable):
    context = serializable.copy()
    for k, v in serializable.items():
        if isinstance(v, dict):
            context[k] = _get_deserialized_instance_of_model(v)
        elif isinstance(v, (list, QuerySet)):
            context[k] = [_get_deserialized_instance_of_model(item) for item in v]
    return context


def _get_serialized_instance_of_model(instance):
    if not isinstance(instance, Model):
        return instance
    app_name = instance._meta.app_label
    model_name = instance._meta.model_name
    return {"app": app_name,
            "model": model_name,
            "pk": instance.pk}


def serialize_context(context):
    serializable = context.copy()
    for k, v in context.items():
        if isinstance(v, Model):
            serializable[k] = _get_serialized_instance_of_model(v)
        elif isinstance(v, (list, set, QuerySet)):
            serializable[k] = [_get_serialized_instance_of_model(item) for item in v]
    return serializable


class AbstractEmailSender:
    template_name = ''
    subject = ''
    always_send = False  # ignore notification settings. For reset password etc
    notification_type_in_user_settings = None
    end_of_the_day_combined_class = None
    end_of_the_day_notification_type = None

    def __init__(self, context=None, subject=None):
        self.context = context or {}

    def get_context(self):
        context = self.context.copy()
        context['subject'] = self.subject
        context['frontend_url'] = os.getenv('FRONTEND_URL')
        context['backend_url'] = os.getenv('BACKEND_URL')
        if url := getattr(self, 'url', None):
            context['url'] = url
        return context

    def can_send_notification(self, user):
        if self.notification_type_in_user_settings:
            return True

        return True

    @classmethod
    def run(cls, params, ignore_end_of_the_day=False):
        to = params['to']

        if not to:
            return
        self = cls(context=params)
        if isinstance(to, models.User):
            user = models.User.objects.get(pk=to.pk)
            if not self.can_send_notification(to):
                return
            if not to.is_active:
                return

            if user.notifications_when == constants.NotificationsWhen.never:
                return

            if user.notifications_when == constants.NotificationsWhen.end_of_the_day:
                pass

            if to.full_name:
                email = f'{clean_name_for_email(to.full_name)} <{to.email}>'
            else:
                email = to.email

        else:
            email = to

        context = serialize_context(self.get_context())
        kwargs = dict(
            template_name=self.template_name,
            context=context,
            subject=self.get_subject(),
            to=email,
        )

        send.apply_async(kwargs=kwargs, countdown=10)

    def get_subject(self):
        if '{' in self.subject:
            return self.subject.format(**self.get_context())
        return self.subject


