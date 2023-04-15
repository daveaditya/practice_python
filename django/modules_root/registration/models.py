from datetime import datetime, timedelta

from django.db import models

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.http import urlencode
from django_twilio.client import twilio_client

from . import utils
from .verification import request as vrequest


class UserManager(models.Manager):
	def create_user(self, first_name, last_name, password, email, mobile_number):
		user = self.create(
			first_name = first_name,
			last_name = last_name, 
			password = make_password(password),
			email = email,
			mobile_number = mobile_number
		)
		return user


class EmailVerificationManager(models.Manager):
	def create_email_verification(self, user, email, code):
		email_verification = self.create(
			user = user,
			email = email,
			code = code
		)
		return email_verification


class MobileVerificationManager(models.Manager):
	def create_mobile_verification(self, user, mobile_number, otp):
		mobile_verification = self.create(
			user = user,
			mobile_number = mobile_number,
			otp = otp
		)
		return mobile_verification


class User(models.Model):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	password = models.CharField(max_length=256)
	email = models.CharField(max_length=200, unique=True)
	mobile_number = models.CharField(max_length=15, unique=True)
	is_admin_verified = models.BooleanField(default=False)
	is_email_verified = models.BooleanField(default=False)
	is_mobile_verified = models.BooleanField(default=False)
	email_verified_at = models.DateTimeField('email verified at', default=None, null=True)
	mobile_verified_at = models.DateTimeField('mobile verified at', default=None, null=True)
	created_at = models.DateTimeField('created at', auto_now_add=True)
	updated_at = models.DateTimeField('updated at', auto_now=True)

	objects = UserManager()

	def send_verification_mail(self):
		vrequest.email_verification(self, self.email)

	def send_otp(self):
		vrequest.mobile_verification(self, self.mobile_number)

	def __str__(self):
		print(f'{self.first_name} {self.last_name}, {self.email}, {self.mobile_number}')


	class Meta:
		db_table = 'modules_user'


class EmailVerification(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE
	)
	email = models.CharField(max_length=200)
	code = models.CharField(max_length=200)
	expires = models.DateTimeField(default=(datetime.now() + timedelta(days=0, hours=0, minutes=59, seconds=60)))
	created_at = models.DateTimeField('created at', auto_now_add=True)
	updated_at = models.DateTimeField('updated at', auto_now=True)

	objects = EmailVerificationManager()

	def send_verification_mail(self):
		send_mail(
			subject="Email Verification", 
			message=None,
			html_message=f"""
			Please click on the following link to verify your email address: 
			<a href="{reverse('verify-email')}?{urlencode({'id': self.user.id, 'code': self.code})}">Click Here</a>
			""",
			from_email="testappid2015@gmail.com",
			recipient_list=[self.email]
		)

	def __str__(self):
		print(f'{self.user.first_name} {self.user.last_name}, {self.email}, {self.code}')


	class Meta:
		db_table = 'modules_email_verification'



class MobileVerification(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE
	)
	mobile = models.CharField(max_length=15)
	otp = models.CharField(max_length=6)
	expires = models.DateTimeField(default=(datetime.now() + timedelta(days=0, hours=0, minutes=4, seconds=59)))
	created_at = models.DateTimeField('created at', auto_now_add=True)
	updated_at = models.DateTimeField('updated at', auto_now=True)

	objects = MobileVerificationManager()

	def send_otp(self):
		message = twilio_client.messages.create(to=self.mobile_number, body=f'The One Time Password(OTP) for verifying your phone number is {self.otp}.')
		message.sid


	def __str__(self):
		print(f'{self.user.first_name} {self.user.last_name}, {self.mobile_number}, {self.code}')


	class Meta:
		db_table = 'modules_mobile_verification'