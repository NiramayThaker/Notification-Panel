from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class UserNotification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	msg_id = models.IntegerField(primary_key=True)
	notification = models.CharField(max_length=10)
	read = models.CharField(max_length=100, default=0)
	unread = models.CharField(max_length=100, default=1)
	all_read = models.BooleanField()

	def __str__(self):
		return f"{self.user} - {self.notification}"


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

