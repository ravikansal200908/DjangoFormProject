import os
from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField()


def validate_file_size(value):
    print("inside validate_file_size.")
    print(f'{value=}')
    limit = 2 * 1024 * 1024  # 2 MB
    if value.size > limit:
        raise ValidationError('File size must be no more than 2 MB.')


def validate_file_extension(value):
    print("inside validate_file_extension.")
    print(f'{value=}')
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions:
        str_e = 'Invalid file extension. Allowed extensions .jpg, .jpeg, .png.'
        raise ValidationError(str_e)


class UserForm(forms.Form):
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    hobbies_choices = [
        ('reading', 'Reading'),
        ('traveling', 'Traveling'),
        ('coding', 'Coding')
        ]

    # Text Input
    username = forms.CharField(max_length=100, help_text="Enter your username")

    # Email Input
    email = forms.EmailField(
        help_text="We'll never share your email with anyone else."
        )

    # Password Input
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text="Choose a strong password"
        )

    # Integer Input
    age = forms.IntegerField(
        help_text="Enter your age",
        min_value=18,  # Specify the minimum allowed age
        max_value=99,   # Specify the maximum allowed age
        initial=10
        )

    # Boolean Field (Checkbox)
    # subscribe_newsletter = forms.BooleanField(
    #     required=False,
    #     initial=True,
    #     help_text="Subscribe to our newsletter"
    #     )

    # Date Input
    birth_date = forms.DateField(help_text="Enter your date of birth")

    # Choice Field (Dropdown)
    gender = forms.ChoiceField(
        choices=gender_choices,
        widget=forms.RadioSelect,
        help_text="Select your gender"
        )

    # Below one will create drop down in the frontend
    # gender = forms.ChoiceField(
    #     choices=gender_choices,
    #     help_text="Select your gender"
    #     )

    # Multiple Choice Field (Checkbox Select Multiple)
    hobbies = forms.MultipleChoiceField(
        choices=hobbies_choices,
        widget=forms.CheckboxSelectMultiple,
        help_text="Select your hobbies"
        )

    # File Input
    profile_picture = forms.ImageField(
        help_text="Upload your profile picture",
        validators=[validate_file_size, validate_file_extension]
        )

    # Decimal Input
    salary = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        initial=10000,
        validators=[
            MinValueValidator(limit_value=0, message='Salary must be  >0'),
            MaxValueValidator(limit_value=100000, message='Salary < 100000'),
        ]
        )

    # Float Input
    height = forms.FloatField(
        help_text="Enter your height in meters",
        validators=[
            MinValueValidator(limit_value=1.52, message='Height > 1.52'),
            MaxValueValidator(limit_value=2.13, message='Height < 2.13'),
        ]
        )

    # Slug Field
    slug = forms.SlugField(help_text="Enter a slug for the URL")

    # Hidden Input
    # hidden_field = forms.CharField(
    #     widget=forms.HiddenInput,
    #     initial="hidden_value",
    #     help_text="This is a hidden field"
    #     )

    # URL Input with validation pattern
    social_media_url = forms.URLField(
        help_text="Enter your social media URL",
        required=False
        )

    feedback = forms.CharField(
        # widget=forms.Textarea,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        help_text="Provide your feedback"
        )

    def clean_age(self):
        print("inside clean_age")
        age = self.cleaned_data['age']
        if not (18 <= age <= 30):
            raise ValidationError("Age must be between 18 and 30.")
        return age

    def clean_birth_date(self):
        print("inside clean_birth_date")
        birth_date = self.cleaned_data['birth_date']
        today = date.today()
        age = (
            today.year - birth_date.year -
            ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        if not (18 <= age <= 60):
            raise ValidationError("You must be between 18 and 60 years old.")
        return birth_date

    def clean_hobbies(self):
        print("inside clean_hobbies")
        hobbies = self.cleaned_data['hobbies']
        if len(hobbies) > 2:
            raise ValidationError("You can choose up to 2 hobbies.")
        return hobbies

    def clean_profile_picture(self):
        print("inside clean_profile_picture")
        # profile_picture = self.cleaned_data['profile_picture']
        # if profile_picture and profile_picture.size > 2 * 1024 * 1024:
        #     raise ValidationError(
        #         "Profile picture size should be between 1 MB and 2 MB."
        #         )
        return self.cleaned_data['profile_picture']

    def clean_slug(self):
        print("inside clean_slug")
        username = self.cleaned_data.get('username', '')
        return username.lower().replace(' ', '-')
