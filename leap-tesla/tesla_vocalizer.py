from vocalizer import Vocalizer
from tesla_wrapper import TeslaWrapper

class TeslaVocalizer(object):
	def __init__(self, is_local=True):
		self.vocalizer = Vocalizer()
		self.wrapper = TeslaWrapper(is_local)

	def response_success_checker(self, response):
		if response:
			if "result" in response:
				if response["result"] == True:
					return True
		return False

	def get_mobile_enabled(self):
		r = self.wrapper.get_mobile_enabled()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Mobile access is enabled.")
		else:
			self.vocalizer.vocalize("Mobile access is not enabled.")

	def open_charge_port_door(self):
		r = self.wrapper.open_charge_port_door()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Opening charge port door.")
		else:
			self.vocalizer.vocalize("Unable to open charge port door.")

	def start_charge(self):
		r = self.wrapper.start_charge()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Starting to charge the vehicle.")
		else:
			self.vocalizer.vocalize("Unable to charge the vehicle.")

	def stop_charge(self):
		r = self.wrapper.stop_charge()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Stopping charging of vehicle.")
		else:
			self.vocalizer.vocalize("Unable to stop charging the vehicle.")

	def flash_lights(self):
		r = self.wrapper.flash_lights()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Flashing the lights once.")
		else:
			self.vocalizer.vocalize("Unable to flash the lights.")

	def honk_horn(self):
		r = self.wrapper.honk_horn()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Honking the horn.")
		else:
			self.vocalizer.vocalize("Unable to honk the horn.")

	def unlock_door(self):
		r = self.wrapper.unlock_door()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Unlocking the doors.")
		else:
			self.vocalizer.vocalize("Unable to unlock the doors.")

	def lock_door(self):
		r = self.wrapper.lock_door()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Locking the doors.")
		else:
			self.vocalizer.vocalize("Unable to lock the doors.")

	def open_sun_roof(self):
		r = self.wrapper.open_sun_roof()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Opening the sun roof.")
		else:
			self.vocalizer.vocalize("Unable to open the sun roof.")

	def close_sun_roof(self):
		r = self.wrapper.close_sun_roof()
		if self.response_success_checker(r):
			self.vocalizer.vocalize("Closing the sun roof.")
		else:
			self.vocalizer.vocalize("Unable to close the sun roof.")

def main():
	t = TeslaVocalizer()
	t.get_mobile_enabled()
	t.open_charge_port_door()
	t.start_charge()
	t.stop_charge()
	t.flash_lights()
	t.honk_horn()
	t.unlock_door()
	t.lock_door()
	t.open_sun_roof()
	t.close_sun_roof()

if __name__ == '__main__':
	main()




