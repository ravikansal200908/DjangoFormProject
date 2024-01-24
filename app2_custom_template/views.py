from django.shortcuts import redirect, render
from .forms import BlogPostForm, UserForm


def blog_post_form(request):  # sourcery skip: extract-method
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        # print(f"{form.is_valid()=}")
        # form_data = form.cleaned_data
        # print(f"{form_data=}")
        # print(f"{form.is_valid()=}")
        print("Before valid")
        if form.is_valid():
            form_data = form.cleaned_data
            print(f"{form_data=}")
            print("Form is valid")
            return redirect('app1:thanks')
    else:
        form = BlogPostForm()
        print(f'{form=}')

    return render(request, "blog_post_form.html", {"form": form})


def user_form(request):
    if request.method == "POST":
        print(f'{request.POST=}')
        print(f'{request.FILES=}')
        form = UserForm(request.POST, request.FILES)
        print("Before valid")
        if form.is_valid():
            form_data = form.cleaned_data
            print(f"{form_data=}")
            print("Form is valid")
            return redirect('app1:thanks')
        else:
            # Print errors to the console or log them
            print(f'{form.errors=}')
    else:
        form = UserForm()
        print(f'{form=}')

    return render(request, "user_form.html", {"form": form})
