from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import json
import logging

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



logger = logging.getLogger(__name__)


def home(request):
    '''Remove extra white spaces'''
    context = {'pagename': 'Hello man', 'name':'imran',}
    template = "pages/home.html"

    return render(request, template, context)


def contact_view(request):
    ''' Handle contact form submission via AJAX and send email.
        and also send JSON response back to the front end site which shows message.
    '''
    if request.method == 'POST':
        try:
            # Parse JSON data from request
            data = json.loads(request.body)
            form = ContactForm(data)
            
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                form_message = form.cleaned_data['message']
                
                # Using SendGrid to send email
                message = Mail(
                    from_email=settings.SENDGRID_FROM_EMAIL,
                    to_emails='squalporeover.ju@gmail.com',
                    subject= f'From portfolio site {name}',
                    html_content=f'<strong>{form_message}<br></br>{email}</strong>'
                    )

                try:
                    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                    response = sg.send(message)
                       
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your message has been sent successfully!'
                    })
                except Exception as e:
                    logger.error(f'Error sending email: {e}')

                    return JsonResponse({
                        'status': 'error',
                        'message': 'Failed to send email. Please try again later.'
                    }, status=500)

            else:
                return JsonResponse(
                    {'status': 'error',
                    'message': 'Please fill in all fields correctly.',
                    'errors': form.errors}, 
                    status=400)
                
        except json.JSONDecodeError:

            return JsonResponse({
                'status': 'error',
                'message': 'Invalid request data.'
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    }, status=405)


    

