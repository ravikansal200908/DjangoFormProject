from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import NameForm, ContactForm, CommentForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect("/thanks/")
            return redirect('app1:thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print(f'{form=}')

    return render(request, "name.html", {"form": form})


def contact_form(request):  # sourcery skip: extract-method
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["info@example.com"]
            if cc_myself:
                recipients.append(sender)

            print(f'{subject=}')
            print(f'{message=}')
            print(f'{sender=}')
            print(f'{cc_myself=}')
            print(f'{recipients=}')

            return redirect('app1:thanks')
    else:
        form = ContactForm()
        print(f'{form=}')

    return render(request, "contact_form.html", {"form": form})


def comment_form(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            return redirect('app1:thanks')
    else:
        form = CommentForm()
        print(f'{form=}')

    return render(request, "comment_form.html", {"form": form})


def thanks(request):
    return HttpResponse("This is thanks page.")
