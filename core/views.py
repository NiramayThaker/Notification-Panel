from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import UserNotification
from django.contrib.auth.models import User


@login_required(login_url='/login')
def index(request):
	return render(request, 'core/index_new.html')


def sign_up(request):
	form = RegistrationForm()

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)

			return redirect('/')

	context = {'form': form}
	return render(request, 'registration/signup.html', context=context)


@login_required(login_url='/login')
def notification_page(request):
	notification = UserNotification.objects.filter(user=request.user)

	context = {"notification": notification}
	return render(request, 'core/notification_new.html', context=context)


@login_required(login_url='/login')
def notification(request, pk):
	notes = UserNotification.objects.get(msg_id=pk)
	
	notes.read = 1
	notes.unread = 0
	notes.save()

	return render(request, 'notification.html')



@login_required(login_url='/login')
def read_all(request):
	notes = UserNotification.objects.filter(user=request.user)
	for note in notes:
		note.read = 1
		note.unread = 0
		note.save()
	return redirect('notification-page')


@login_required(login_url='/login')
def note(request, pk):
	note = UserNotification.objects.get(msg_id=pk)
	note.read = 1
	note.unread = 0
	note.save()

	context = {"note": note}
	return render(request, 'core/note.html', context=context)

