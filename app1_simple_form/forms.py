from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class CommentForm(forms.Form):
    name = forms.CharField(label="Your name", initial="Your name")
    url = forms.URLField(label="Website", required=False, initial="http://")
    comment = forms.CharField()
    captcha_answer = forms.IntegerField(label="2 + 2", label_suffix=" =")
