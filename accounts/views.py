from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView
from django.views.generic.edit import UpdateView

from .models import CustomUser

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    """Sign Up View"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Profile View"""

    model = CustomUser
    success_url = reverse_lazy("twit_list")
    template_name = "profile.html"
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "date_of_birth",
    )

    def test_func(self):
        """User passes test function authorization"""
        obj = self.get_object()
        return obj == self.request.user


class PublicProfileView(LoginRequiredMixin, DetailView):
    """Public Profile View"""

    model = CustomUser
    template_name = "public_profile.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Profile Update View """

    model = CustomUser
    template_name = "profile_edit.html"
    success_url = reverse_lazy('accounts:profile')
    fields = ["first_name", "last_name", "date_of_birth", "email", "username"]

    def test_func(self):
        """User passes test function authorization"""
        obj = self.get_object()
        return obj.user == self.request.user
""" 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super (ProfileUpdateView, self).form_valid(form) """