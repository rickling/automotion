from vocalizer import Vocalizer
from twilio_wrapper import TwilioWrapper

class TwilioVocalizer(object):
	def __init__(self):
		self.wrapper = TwilioWrapper()
		self.vocalizer = Vocalizer()

	def vocalize(self, action_type, number, message):
		statement = "I am now %s number %s" % (action_type, number)
		if action_type == "messaging":
			self.wrapper.message_home(message)
			statement += " with message %s" % message
		elif action_type == "calling":
			self.wrapper.call_home()
		self.vocalizer.vocalize(statement)

if __name__ == '__main__':
    main()

def main():
	twilio_vocalizer = TwilioVocalizer()
    twilio_vocalizer.vocalize("messaging", "+14695855530", "I like pie")
    twilio_vocalizer.vocalize("calling", "+14695855530")