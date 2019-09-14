'''
This is an app that uses CV to identify if a bird is about to fly and take pictures using a Canon brand camera maybe other brands too
'''

'''
better with Javascript?
C++
Java?
'''

'''
What do  i need to do for this too work?
CV with enough training data to identify flying birds
	Check if in flight by examining if its spreads its wings from a stationary position
	if possible check by using the before flight jumping motion; need to find the difference between that motion and other motions like another bird hitting branch 
	wind blowing the branch etc

access the camera monitoring feature and run analysis on it
	access the camera monitoring and then store it into some kind of data dump and then run analysis on it.
	run this analysis every second or so, so i need something that keeps track of time. 
	i should probably set something that auto shutsdown at the time that 
		a. the camera is shut off
		b. camera is moved
		c. when the sun sets based on timezone/ place on earth
	should have some kind of on/off mechanism for this too work

have access to the snapshot button maybe thru the use of bluetooth connections.
	look into how the wireless camera button remotes work 

optional features:
allow for automatic changing of focus. lighting
follow the birds flight if possible

'''

from time import*


class Camera_AI():

	def __init__(self):
		self._on = True 
		self._camera_data = 0
		self._time = 0
		self._auto = False
		self._bluetooth = False

	def access_camera(self):
		return 0

	def take_pictures(self):
		return 0

	def run_CV(self):
		return 0

	def time_check(self):
		return 0

	def auto_shutoff(self):
		''' 
		make this optional
		'''
		return 0

	def on_off(self):

		return 0

	def connect_to_bluetooth(self):
		return 0