from .. import utils
from .. import models


def email_verification(user, email):
	email_verification = models.EmailVerification.objects.create_email_verification(
		user = user,
		email = email,
		code = utils.generate_activation_key(email)
	)
	email_verification.send_verification_mail()
	email_verification.save()

def mobile_verification(user, mobile_number):
	mobile_verification = models.MobileVerification.objects.create_mobile_verification(
		user = user,
		mobile_number = mobile_number,
		otp = utils.generate_otp(6)
	)
	mobile_verification.send_otp()
	mobile_verification.save()