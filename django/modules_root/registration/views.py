from django.http import Http404
from django.shortcuts import render
from django.core.mail import send_mail

from django.contrib.auth.hashers import make_password, check_password

from . import models
from . import utils

# Create your views here.
def index(request):
	return render(request, 'registration/form.html', {})


def register(request):
	if request.method == 'POST':
		post = dict(request.POST.dict())
		
		# Create user
		user = models.User.objects.create_user(
			first_name=post['first_name'],
			last_name=post['last_name'],
			password=make_password(request.POST.get('password')),
			email=post['email'],
			mobile_number=post['mobile_number']
		)

		# Save user
		user.save()

		# send verification email
		user.send_verification_mail()

		return render(request, 'registration/success.html', {'data': post})
	else:
		return Http404()