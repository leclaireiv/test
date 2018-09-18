def dfparse(str):
	tup = (False, [])
	done = False
	test = 'S'

	while not done: # while string isn't same as input


		bt = False # Backtracking flag
		for i in range(len(test)): # See if backtracking needs to occur

			if (len(test.replace('S', '')) > len(str)) or (not 'S' in test and test != str): # If string is already larger than the input OR is fully terminal and wrong
				bt = True
				break
			if test[i] == 'S': # Valid Left to Right so far
				break
			if test[i] == str[i]: # Current char is valid
				continue
			else: # Catch all
				bt = True
				break



		if bt: # Backtracking loop
			for i in range(len(tup[1])-1, -1, -1):	#Work  backwards through the list of moves made

				# Moves are attempted in order (1, 2, then 3)

				if tup[1][i][0] == 3:	# If the last move was 3, then all potential moves have already been exhausted. Look back further
					del tup[1][-1]
					continue

				if tup[1][i][0] == 2:	# If the last move was 2, back track and try 3
					test = tup[1][i][1]
					test = test.replace('S', '', 1)
					newtup = (3, tup[1][i][1])
					tup[1][i] = newtup
					break

				if tup[1][i][0] == 1:	# If the last move was 1, back track and try 2
					test = tup[1][i][1]
					test = test.replace('S', 'bSaS', 1)
					newtup = (2, tup[1][i][1])
					tup[1][i] = newtup
					break

		else:	# Found a new state, try move 1
			tup[1].append((1, test))
			test = test.replace('S', 'aSbS', 1)

		if test == str or test == '':	# Checks for solution
			done = True

	if test == str:
		retTup = (True, [])	# Organize the return tuple
		for i in range(len(tup[1])):
			retTup[1].append(tup[1][i])

	else:
		retTup = (False, [])
		
	return retTup


print dfparse('babbba')

