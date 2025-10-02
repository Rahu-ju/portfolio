from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import json
import logging


logger = logging.getLogger(__name__)
# all the views here

def home(request):

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
                message = form.cleaned_data['message']
                
                # Compose email
                subject = f'Contact Form Message from {name}'
                email_message = f"""
                    New contact form submission:
                    Name: {name}
                    Email: {email}

                    Message:
                    {message}
                """
                
                try:
                    send_mail(
                        subject,
                        email_message,
                        settings.EMAIL_HOST_USER,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                    )
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your message has been sent successfully!'
                    })
                except Exception as e:
                    logger.exception('Error sending email: %s', e)
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


    

