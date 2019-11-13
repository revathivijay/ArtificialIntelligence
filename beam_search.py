def change_one_bit(current_state):
	next_states = []
	for i in range(4):
		current = current_state.copy()
		if current[i] == 0:
			current[i] = 1
		else:
			current[i] = 0
		next_states.append(current)
	state_scores = []
	for i in range(4):
		score = calculate_score(next_states[i], final_state)
		state_scores.append([next_states[i], score])
	print("Next possible states: ", state_scores)
	state_scores = Sort(state_scores)
	print("Sorting based on scores: ")
	print(state_scores)
	next_state = []
	next_state.append(state_scores[0][0])
	next_state.append(state_scores[1][0])
	print("Choosing best states: ", next_state)
	return next_state

def calculate_score(current_state, final_state):
	count = 0
	for i in range(4):
		count += int(current_state[i]) ^ int(final_state[i])
	return count

def get_states():
	print("Enter Initial state")
	initial_state = [int(x) for x in input().split()]
	print("Enter final state")
	final_state = [int(x) for x in input().split()]
	return initial_state, final_state

def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 

def beam_search(initial_state, final_state):
	current_state = initial_state.copy()
	next_states = []
	path = []
	path.append(initial_state)
	while current_state!=final_state:
		next_states = change_one_bit(current_state)
		current_state = next_states[0]
		path.append(current_state)
	path.append(final_state)
	
	print("Goal state reached via following path")
	print(path[:-1])

if __name__ == '__main__':
	initial_state, final_state = get_states()
	beam_search(initial_state, final_state)

