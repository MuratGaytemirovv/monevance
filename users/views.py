from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
