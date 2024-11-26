rules.add(all valid states in states)
rules.add(all ingame in characters)
rules.add(all wavedashing in grounded)
rules.add(all off screen not in grounded and in ingame)
rules.add(all attacking in ingame)
rules.add(all moving in ingame)
rules.add(all shielding in ingame)
rules.add(all tiltattacking in attacking)
rules.add(all haswavedashmomentum in ingame)
rules.add(all item in itemruleset)
rules.add(all rules in game)

assert all rules
while True:
	try:
		next(iter(validstates))(inputs)