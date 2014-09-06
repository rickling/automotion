import requests

class TeslaWrapper(object):
	""" Python Wrapper for the Tesla API """
	def __init__(self):
		self.url = "http://localhost:8080/mockTesla/"
		self.session = requests.session()

	def login(self):
		self.session.post(self.url + "/login")

	def vehicles(self):
		#stuff

	def set_my_vehicle_id(self, vehicle_id):
		#stuff


	# Vehicle Statuses
	def get_mobile_enabled(self, vehicle_id=None):
		#stuff

	def get_charge_state(self, vehicle_id=None):
		#stuff

	def get_climate_state(self, vehicle_id=None):
		#stuff

	def get_drive_state(self, vehicle_id=None):
		#stuff

	def get_gui_settings(self, vehicle_id=None):
		#stuff

	def get_vehicle_state(self, vehicle_id=None):
		#stuff

	# Vehicle Commands
	def open_charge_port_door(self, vehicle_id=None):
		#stuff

	def set_charge_to_standard(self, vehicle_id=None):
		#stuff

	def set_charge_to_max(self, vehicle_id=None):
		#stuff

	def set_charge_limit(self, vehicle_id=None, limit_value):
		#stuff

	def start_charge(self, vehicle_id=None):
		#stuff

	def stop_charge(self, vehicle_id=None):
		#stuff

	def flash_lights(self, vehicle_id=None):
		#stuff

	def honk_horn(self, vehicle_id=None):
		#stuff

	def unlock_door(self, vehicle_id=None):
		#stuff

	def lock_door(self, vehicle_id=None):
		#stuff

	def set_temperature(self, vehicle_id=None, driver_degC, pass_degC):
		#stuff

	def start_AC(self, vehicle_id=None):
		#stuff

	def stop_AC(self, vehicle_id=None):
		#stuff

	def open_sun_roof(self, vehicle_id=None):
		#open

	def close_sun_roof(self, vehicle_id=None):
		#close





