from agent import VacuumAgent
import unittest

class Unit_Test(unittest.TestCase):

	def test(self):
		vac = VacuumAgent()
		self.assertEqual(vac.tester(["Dirty", "Dirty"], 0, []), ["Suck", "Right", "Suck"])

if __name__  == '__main__':
	unittest.main()
