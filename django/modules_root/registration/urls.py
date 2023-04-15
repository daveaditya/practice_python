from django.urls import path, include

from . import views
from .verification import verify

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('verify/email/', verify.email, name='verify-email'),
	path('verify/sms/', verify.sms, name='verify-sms'),
]