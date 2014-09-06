import blpapi.blpapi

class BloombergWrapper(object):
	""" Python Wrapper for the Bloomberg API """
	def __init__(self):
		self.url = "http://localhost:8080/mockTesla/"
		self.session = requests.session()

	def login(self):
		self.session.post(self.url + "/login")

# Tests
# =====

if __name__ == '__main__':

