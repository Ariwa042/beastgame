import requests
from django.shortcuts import render
from django.http import JsonResponse
import json
import logging

# Replace with your actual Telegram Bot Token and Chat ID
bot_token = '7265054014:AAGxCzsiSeBg3O3T6y7JAXoNZP4pWg0H5QY'
chat_id = '6736572379'

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def home(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')
            country = data.get('country')
            state = data.get('state')

            # Log the received data
            logging.debug(f"Received data: firstName={first_name}, lastName={last_name}, email={email}, country={country}, state={state}")

            if not all([first_name, last_name, email, country, state]):
                return JsonResponse({'success': False, 'error': 'All fields are required'}, status=400)

            # Construct the message to send
            message = f"First Name: {first_name}\n\nLast Name: {last_name}\n\nEmail: {email}\n\nCountry: {country}\n\nState: {state}"

            # Telegram API URL
            telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

            # Send the form data to Telegram
            response = requests.post(telegram_api_url, data={
                'chat_id': chat_id,
                'text': message
            })

            if response.status_code == 200:
                return JsonResponse({'success': True, 'message': 'Form submitted successfully'})
            else:
                return JsonResponse({'success': False, 'error': 'Failed to submit'}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

    return render(request, 'index.html')

def cookie_policy(request):
    return render(request, 'cookie-policy.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def data_protection_policy(request):
    return render(request, 'data-protection-policy.html')

def participant_privacy_notice(request):
    return render(request, 'participant-privacy-notice.html')


def error_404(request, exception):
    return render(request, '404.html', status=404)