#from django import newforms as forms
from django import forms

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea(),initial="Replace with your feedback")
    sender = forms.EmailField(required=False)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
	print "aaa"
    else:
        form = ContactForm()
	print "bbb"
    return render_to_response('contact.html', {'form': form})
