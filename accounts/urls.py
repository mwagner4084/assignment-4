from django.urls import path

from .views import SignUpView, ProfileView, ProfileUpdateView, PublicProfileView
app_name = 'accounts'

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("profile/<int:pk>/edit", ProfileUpdateView.as_view(), name="profile_edit"),
    path("public/profile/<int:pk>/", PublicProfileView.as_view(), name="public_profile"),
]
