from agent import VacuumAgent
import unittest

class Unit_Test(unittest.TestCase):

	def test(self):
		vac = VacuumAgent()
		self.assertTrue(vac.tester(["Clean", "Dirty"], 0, 0, []), ["Suck", "Right"])

if __name__  == '__main__':
	unittest.main()
