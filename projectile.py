"""
Definition of Projectile Class

@author: Mathieu Adam <adammathieu@gmail.com>
@license: Python
@version: '0.1'
"""

from math import cos
from math import sin
from math import tan
from numpy import arange

g = 9.8

class Projectile(object):
	"""
    Class Projectile defines projectile trajectory calculation methods.
    """

	def __init__(self, angle, power, px, py, masse = 200):
		self.angle = angle
		self.vx0 = power * cos(angle) #Initial Velocity X
		self.vy0 = power * sin(angle) #Initial Velocity Y
		self.x0 = px #Position X0
		self.y0 = py #Position Y0
		self.x = self.x0
		self.y = self.y0
		self.masse = masse

	def updatePosition(self, t):
		self.x = self.x0 + self.vx0*t
		self.y = self.y0 + self.vy0*t -0.5*g*t*t

	def displayPosition(self):
		print self.x,self.y

if __name__ == "__main__":
	boulet = Projectile(45,8,0,0,100)
	for t in arange(0,10,0.1):
		boulet.updatePosition(t)
		if(boulet.y>=0):
			boulet.displayPosition()
		else:
			break