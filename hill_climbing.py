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
	print("Choosing best state: ", state_scores[0])
	next_state = state_scores[0][0]
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

def hill_climbing(initial_state, final_state):
	current_state = initial_state.copy()
	while current_state!=final_state:
		current_state = change_one_bit(current_state)
	print("Goal state reached")

if __name__ == '__main__':
	initial_state, final_state = get_states()
	hill_climbing(initial_state, final_state)

