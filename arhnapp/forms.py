from django import forms
from .models import aarohanparticipant#workshopparticipant


# class workshopregForm(forms.ModelForm):
# 	class Meta:
# 		model=workshopparticipant
# 		fields=('participant','college','mobile','email','robotics','robo_pay_status','IoT','IoT_pay_status','IC_Engine','IC_pay_status','payment_mode')


class arhnregform(forms.ModelForm):
	class Meta:
		model=aarohanparticipant
		fields=('participant','college','mobile','email')