from django.shortcuts import render
from django.http import HttpResponseRedirect
from registration import models
from django.urls import reverse

# Create your views here.
def index(request):
	# retrieve user from sesssion
	if 'user_id' in request.session:
		user = models.User.objects.get(pk=request.session['user_id'])
		
		# return profile view
		return render(request, 'mprofile/profile.html', {
			'is_email_verified': user.is_email_verified,
			'email_verified_at': user.email_verified_at,
			'is_mobile_verified': user.is_mobile_verified,
			'mobile_verified_at': user.mobile_verified_at,
		})
	else:
		return HttpResponseRedirect(reverse('login'))