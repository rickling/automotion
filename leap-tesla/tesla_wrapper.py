import requests
import json

class TeslaWrapper(object):
	""" 
		Python Wrapper for the Tesla API.

		Usage:
		t = TeslaWrapper()
		t.login()
		t.set_vehicle_id(123)
	"""

	def __init__(self, is_local=True):
		self.url = "http://localhost:8080/mockTesla/"
		self.vehicle_id = None
		self.session = requests.session()
		if is_local:
			self.login()
			self.set_vehicle_id(1234567890)

	def query_and_output(self, path):
		url = self.url + path
		r  = self.session.post(url)
		self.output(r)

	def output(self, response):
		""" Outputs the httpresponse in a pretty format. """
		try:
			output = response.json()
		except:
			output = {'status_code': response.status_code, 'response_body': response.text}
		print json.dumps(output, sort_keys=True,indent=4, separators=(',', ': '))

	def login(self):
		path = "login"
		self.query_and_output(path)

	def vehicles(self):
		path = "vehicles"
		self.query_and_output(path)

	def set_vehicle_id(self, vehicle_id):
		self.vehicle_id = vehicle_id

	# Vehicle Statuses
	def get_mobile_enabled(self):
		""" Returns Success if mobile access is enabled on the vehicle """
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")
		path = "vehicles/%d/mobile_enabled" % self.vehicle_id 
		self.query_and_output(path)

	def get_charge_state(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/charge_state" % self.vehicle_id 
		self.query_and_output(path)

	def get_climate_state(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/climate_state" % self.vehicle_id 
		self.query_and_output(path)

	def get_drive_state(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/drive_state" % self.vehicle_id 
		self.query_and_output(path)

	def get_gui_settings(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/gui_settings" % self.vehicle_id 
		self.query_and_output(path)

	def get_vehicle_state(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/vehicle_state" % self.vehicle_id 
		self.query_and_output(path)

	# Vehicle Commands
	def open_charge_port_door(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/charge_port_door_open" % self.vehicle_id 
		self.query_and_output(path)

	def set_charge_to_standard(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/charge_standard" % self.vehicle_id 
		self.query_and_output(path)

	def set_charge_to_max(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/charge_max_range" % self.vehicle_id 
		self.query_and_output(path)

	def set_charge_limit(self, limit_value):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/set_charge_limit?percent=%d" % (self.vehicle_id, limit_value)
		self.query_and_output(path)

	def start_charge(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/charge_start" % self.vehicle_id
		self.query_and_output(path)

	def stop_charge(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/charge_start" % self.vehicle_id
		self.query_and_output(path)

	def flash_lights(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/flash_lights" % self.vehicle_id
		self.query_and_output(path)

	def honk_horn(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/honk_horn" % self.vehicle_id
		self.query_and_output(path)

	def unlock_door(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/door_unlock" % self.vehicle_id
		self.query_and_output(path)

	def lock_door(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/door_lock" % self.vehicle_id
		self.query_and_output(path)

	def set_temperature(self, driver_degC, pass_degC):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/set_temps?driver_temp=%d&passenger_temp=%d" % (self.vehicle_id, driver_degC, pass_degC)
		self.query_and_output(path)

	def start_AC(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/auto_conditioning_start" % self.vehicle_id
		self.query_and_output(path)

	def stop_AC(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/auto_conditioning_stop" % self.vehicle_id
		self.query_and_output(path)

	def open_sun_roof(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/sun_roof_control?state=%s" % (self.vehicle_id, "open")
		self.query_and_output(path)

	def close_sun_roof(self):
		if not self.vehicle_id:
			raise ValueError("Please set the vehicle id")	
		path = "vehicles/%d/command/sun_roof_control?state=%s" % (self.vehicle_id, "close")
		self.query_and_output(path)

