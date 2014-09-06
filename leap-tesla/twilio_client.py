from twilio.rest import TwilioRestClient

class TwilioClient(object):
	""" 
		A client that performs messages and calls to home. 

		Usage:
		t = TwilioClient()
		t.message_home_on_my_way()
	"""
	
	def __init__(self):
		account_sid = "AC7d41d8405e0fd56b140f21ec1d83700f"
		auth_token = "1c823da53d96bb417b57b83ab37bbfba"
		self.my_twilio_number = "+14694164097"
		self.my_home_number = "+14695855530"
		self.client = TwilioRestClient(account_sid, auth_token)

	def message_home_on_my_way(self):
		message = self.client.messages.create(body="I'm on my way", 
											  to=self.my_home_number,
											  from_=self.my_twilio_number)
		print message.sid

	def call_home(self):
		call = self.client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
										to=self.my_home_number,
										from_=self.my_twilio_number)
		print call.sid