class VacuumAgent:
 	# def __init__(self)
	#	self.model = { "Left" : None, "Right" : None, "Current" : None}
	def action(self, state, location, cost):
		if state[location] == "Dirty":
			action = "Suck"
			cost = cost + 1
		elif location == 0:
			action = "Right"
			cost = cost + 1
		else:
			action = "Left"
			cost = cost + 1
		return action, cost

	def update(self, action, state, location, cost):
		if action == "Suck":
			state[location] == "Clean"

		elif action == "Right":
			location = 1
		else:
			location = 0
		return state, location

	def result( state):
		if state == ["Clean", "Clean"]:
			return True
		else:
			return False

	def tester(self, state, location, cost, sequence):
		if self.result():
			return sequence
		action = self.action(state, location, cost)
		sequence.append(action)
		state, location = self.update(state, action, location, cost)
