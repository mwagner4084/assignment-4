# Generated by Django 4.0.7 on 2022-12-13 22:05

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=150, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last_name')),
                ('date_of_birth', models.DateField(verbose_name='date_of_birth')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email_address')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='\nRequired. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(default=False, help_text='\nDesignates that this user has all permissions without explicitly assigning them.', verbose_name='superuser_status')),
                ('is_staff', models.BooleanField(default=False, help_text='\nDesignates whether the user can log into this admin site.', verbose_name='staff_status')),
                ('is_active', models.BooleanField(default=True, help_text='\nDesignates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='\nThe groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', related_query_name='customuser', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='\nSpecific permissions for this user.', related_name='customuser_set', related_query_name='customuser', to='auth.permission', verbose_name='user_permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]