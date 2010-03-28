from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name','anonimo')
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')
            send_mail(
                'Feedback desde fabiosouto.eu, nombre: %s' % name,
                message, sender,
                ['fsoutomoure@gmail.com']
            )
            return render_to_response('thanks.html')
    else:
        form = ContactForm()
    return render_to_response('contact.html', {'form': form})
