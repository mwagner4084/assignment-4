"""
Marissa Wagner
CIS 218
12/13/2022

"""

from django.db import models
from django.urls import reverse
import django.contrib.auth.models
import django.contrib.auth.validators
from django.contrib.auth.models import AbstractUser
import django.utils.timezone
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from twits.models import Twit, Comment

class CustomUser(AbstractUser):
    """ Custom User Model """

    first_name = models.CharField(
        max_length=150,
        verbose_name='first name'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='last name'
    )
    date_of_birth = models.DateField(
        default=django.utils.timezone.now,
        null=False,
        blank=False,
    )
    username = models.CharField(
        error_messages={'unique': 'A user with that username already exists.'}, 
        help_text='\nRequired. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', 
        max_length=150, 
        unique=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], 
        verbose_name='username'
    )
    date_joined = models.DateTimeField(default=django.utils.timezone.now)
    last_login = models.DateTimeField(default=django.utils.timezone.now)
    groups = models.ManyToManyField(
        blank=True, 
        help_text='\nThe groups this user belongs to. A user will get all permissions granted to each of their groups.', 
        related_name='customuser_set', 
        related_query_name='customuser', 
        to='auth.group', 
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        blank=True, 
        help_text='\nSpecific permissions for this user.', 
        related_name='customuser_set', 
        related_query_name='customuser', 
        to='auth.permission', 
        verbose_name='user_permissions'
    )
    is_superuser = models.BooleanField(
        default=False, 
        help_text='\nDesignates that this user has all permissions without explicitly assigning them.', 
        verbose_name='superuser_status'
    )
    is_staff = models.BooleanField(
        default=False, 
        help_text='\nDesignates whether the user can log into this admin site.', 
        verbose_name='staff_status'
    )
    is_active = models.BooleanField(
        default=True, 
        help_text='\nDesignates whether this user should be treated as active. Unselect this instead of deleting accounts.', 
        verbose_name='active'
    )

    # all user to login with email
    USERNAME_FIELD = 'username' 
    # username required by default
    REQUIRED_FIELDS = ['email', 'password']

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_joined = timezone.now()
        self.last_login = timezone.now()
        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        """ Return user's Twits """
        if self.username == None:
            return "ERROR - USERNAME IS NULL."
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})

    def twits(self):
        obj = Twit.objects.filter(user=self)
        return obj

    def num_of_twits(self):
        return Twit.objects.filter(user=self).count()
    
    def all_comments(self):
        return Comment.objects.filter(user=self)