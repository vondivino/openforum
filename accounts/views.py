from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.models import User

class ForumLoginView(LoginView):
    template_name = 'registration/login.html'

class ForumSignUpView(CreateView):
    model = User
    fields = (
        'first_name', 'last_name', 
        'username', 'password'
    )
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
