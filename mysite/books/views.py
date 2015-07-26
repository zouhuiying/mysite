from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book
from forms import ContactForm
from django.core.mail import send_mail

from django.http import HttpResponseRedirect

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })

def contact(request):
    #form = ContactForm()
    #return render_to_response('contact.html', {'form': form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')
            send_mail(
                'Feedback from your site, topic: %s' % topic,
                message, sender,
                ['haoningabc@163.com']
            )
            #return HttpResponseRedirect('/contact/thanks/')
            return render_to_response('contact.html', {'form': form})
    else:
        form = ContactForm()
    return render_to_response('contact.html', {'form': form})
