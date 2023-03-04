from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="home"),

	path("home", views.index, name="home"),

	path("signup", views.sign_up, name="sign-up"),

	path("mark-all-as-read/", views.read_all, name="read-all"),

	path("mark-all-as-unread/", views.unread_all, name="unread-all"),

	path("notification-page/", views.notification_page, name="notification-page"),

	path("notification/<str:pk>/", views.notification, name="notification"),

	path("note/<str:pk>/", views.note, name="note"),

	path("signup", views.sign_up, name="sign-up"),
]
