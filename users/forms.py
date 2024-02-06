from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'password1', 'password2','phoneNumber',]



