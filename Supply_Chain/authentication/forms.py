from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = [ 'username', 'email', 'password1', 'password2' ]