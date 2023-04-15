from django.utils.crypto import get_random_string
import hashlib
import math, random

def generate_activation_key(email):
	"""
	Creates activate key for email address
	"""
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	secret_key = get_random_string(20, chars)
	return hashlib.sha256((secret_key + email).encode('utf-8')).hexdigest()

def generate_otp(length):
	"""
	Generates OTP of the given length
	"""
	digits = "0123456789"
	otp =  ""

	for _ in range(length):
		otp += digits[math.floor(random.random() * 10)]

	return otp