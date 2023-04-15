from .. import models
from datetime import datetime

from django.utils.timezone import utc
from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

def email(request):
	if request.method == 'GET':
		user_id = request.GET.get('id')
		code = request.GET.get('code')
		try:
			user = models.User.objects.get(pk=user_id)
			email_verification = models.EmailVerification.objects.get(email = user.email, code = code)
			if (datetime.utcnow().replace(tzinfo=utc) - email_verification.expires).total_seconds() / 3600 < 1:
				user.is_email_verified = True
				user.email_verified_at = datetime.now()
				user.save()
				email_verification.delete()
				return render(request, 'verification/verified.html', {})
			else:
				return render(request, 'verification/failed.html', {})
		except ObjectDoesNotExist:
			raise Http404("No record found.")
	else:
		return render(request, 'verification/failed.html', {})

def sms(request):
	if request.method == 'POST':
		user_id =  request.POST.get('id')
		otp = request.POST.get('otp')
		try:
			user = models.User.objects.get(pk=user_id)
			mobile_verification = models.MobileVerification.objects.get(email = user.email, otp = otp)
			if datetime.now() < mobile_verification.expires:
				user.is_mobile_verified = True
				user.mobile_verified_at = datetime.now()
				user.save()
				mobile_verification.delete()
				return render(request, 'verification/verified.html', {})
			else:
				return render(request, 'verification/failed.html', {})
		except ObjectDoesNotExist:
			raise Http404("No record found.")
	else:
		return render(request, 'verification/failed.html', {})