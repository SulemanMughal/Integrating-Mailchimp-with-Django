
from django.http import JsonResponse
from django.shortcuts import render, redirect

from djangomailchimp import settings
from marketing.forms import EmailForm

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import logging


logger = logging.getLogger(__name__)

mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})


def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)


def subscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                    'merge_fields': {
                    'FNAME': 'Elliot',
                    'LNAME': 'Alderson',
                    }
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                logger.info(f'API call successful: {response}')
                return redirect('subscribe-success')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                return redirect('subscribe-fail')

    return render(request, 'subscribe.html', {
        'form': EmailForm(),
    })


def subscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully subscribed',
        'message': 'Yay, you have been successfully subscribed to our mailing list.',
    })


def subscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Failed to subscribe',
        'message': 'Oops, something went wrong.',
    })

import hashlib

def unsubscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                form_email_hash = hashlib.md5(form_email.encode('utf-8').lower()).hexdigest()
                member_update = {
                    'status': 'unsubscribed',
                }
                response = mailchimp.lists.update_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    form_email_hash,
                    member_update,
                )
                logger.info(f'API call successful: {response}')
                return redirect('unsubscribe-success')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                return redirect('unsubscribe-fail')

    return render(request, 'unsubscribe.html', {
        'form': EmailForm(),
    })


def unsubscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully unsubscribed',
        'message': 'You have been successfully unsubscribed from our mailing list.',
    })


def unsubscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Failed to unsubscribe',
        'message': 'Oops, something went wrong.',
    })


