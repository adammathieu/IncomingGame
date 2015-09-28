"""
Definition of Canon Class

@author: Mathieu Adam <adammathieu@gmail.com>
@license: Python
@version: '0.1'
"""

class Canon(object):
	"""
    Class Canon defines canon trajectory calculation methods.
    """

    def __init__(self, angle = 45, power = 5, px = 0, py = 0):
    	self.angle = angle
    	self.power = power #initial speed (m/s)
    	self.x0 = px
    	self.y0 = py
