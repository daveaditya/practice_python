from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

from registration import models

# Create your views here.
def index(request):
	return render(request, 'login/form.html', {})

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user = models.User.objects.get(email=email)
			print(check_password(password, user.password))
			if check_password(password, user.password):
				# log in the user into session
				request.session['user_id'] = user.id

				# redirect to profile
				return HttpResponseRedirect(reverse('profile'))
			else:
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		except ObjectDoesNotExist:
			raise Http404('No Such User Found.')
	else:
		raise Http404('Unsupported Method.')

def logout(request):
	# remove user from session
	if 'user_id' in request.session:
		del request.session['user_id']

	# redirect user to login page
	return HttpResponseRedirect(reverse('login'))