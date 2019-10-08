import sys
class VacuumAgent:
 	# def __init__(self)
	#	self.model = { "Left" : None, "Right" : None, "Current" : None}
	def action(self, state, location):
		if state[location] == "Dirty":
			action = "Suck"
		elif location == 0:
			action = "Right"
		else:
			action = "Left"
		return action

	def update(self, action, state, location):
		if action == "Suck":
			print(f'CLEANING location {location}!')
			state[location] = "Clean"
			print(state)
		elif action == "Right":
			location = 1
		else:
			location = 0
		return state, location

	def result(self,state):
		print("GOING INTO FUNCTION")
		if state == ["Clean", "Clean"]:
			print("RESULT IS TRUE. SUCCESS!!")
			return True
		else:
			print("RESULT IS FALSE")
			return False

	def tester(self, state, location, sequence):
		while True:
			res = self.result(state)
			print(f"RESULT IS {res}")
			if res:
				return sequence
			'''
			if self.result(state):
				print("Result HERE!")
				return sequence
			'''
			action = self.action(state, location)
			print(f'Action is {action}')
			sequence.append(action)
			print("Updating state and location")
			state, location = self.update(action, state, location)
			print(f'State is {state} and location is {location}')
