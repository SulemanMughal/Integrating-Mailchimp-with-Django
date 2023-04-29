
from django.http import JsonResponse


def send_view(request):
    return JsonResponse({
        'detail': 'This view is going to send an email.',
    })


import mailchimp_transactional
from django.http import JsonResponse
from mailchimp_transactional.api_client import ApiClientError

from djangomailchimp import settings

mailchimp = mailchimp_transactional.Client(
    api_key=settings.MAILCHIMP_TRANSACTIONAL_API_KEY,
)


def mailchimp_transactional_ping_view(request):
    try:
        mailchimp.users.ping()
        return JsonResponse({
            'detail': 'Everything is working fine',
        })
    except ApiClientError as error:
        return JsonResponse({
            'detail': 'Something went wrong',
            'error': error.text,
        })
    

def send_view(request):
    message = {
        'from_email': '<YOUR_SENDER_EMAIL>',
        'subject': 'My First Email',
        'text': 'Hey there, this email has been sent via Mailchimp Transactional API.',
        'to': [
            {
                'email': 'futuresoftcode@gmail.com',
                'type': 'futuresoftcode@gmail.com'
            },
        ]
    }
    try:
        response = mailchimp.messages.send({
            'message': message,
        })
        return JsonResponse({
            'detail': 'Email has been sent',
            'response': response,
        })
    except ApiClientError as error:
        return JsonResponse({
            'detail': 'Something went wrong',
            'error': error.text,
        })