import random
from time import sleep

def get_states():
	print("Enter Initial state")
	initial_state = [int(x) for x in input().split()]
	print("Enter final state")
	final_state = [int(x) for x in input().split()]
	return initial_state, final_state

def change_one_bit(current_state, tabu, moves):
	
	i = random.randint(0,3)
	index = i
	if tabu[i] > 5:
		while tabu[index]<=5:
			index = random.randint(0,3)
		tabu[i] = 0
	print("Changing index ", index)
	if current_state[index]==0:
		current_state[index] = 1 
	else:
		current_state[index] = 0
	tabu[index]+=1
	moves+=1
	return current_state, tabu, moves

def change_two_bits(current_state, tabu, moves):
	i,j= random.sample(range(0,4), 2)
	index1 = i
	index2 = j
	if tabu[i]>5 and tabu[j]<=5:
		while tabu[index1]<=5 and index1!=j:
			index1 = random.randint(0,3)
		tabu[i] = 0

	if tabu[j]>5 and tabu[i]<=5:
		while tabu[index2]<=5 and index2!=j:
			index2 = random.randint(0,3)
		tabu[j] = 0

	if tabu[i]>5 and tabu[j]>5:
		while tabu[index1] <=5 and tabu[index2] <=5:
			index1, index2 = random.sample(range(0,4), 2)
		tabu[j] = tabu[i] = 0

	print("Changing indices", index1 , " and ", index2)
	if current_state[index1]==0:
		current_state[index1] = 1
	else:
		current_state[index1] = 0

	if current_state[index2]==0:
		current_state[index2] = 1
	else:
		current_state[index2] = 0

	tabu[index1]+=1
	tabu[index2]+=1
	moves+=1

	return current_state, tabu, moves

def tabu(initial_state, final_state):
	tabu = [0, 0, 0, 0]
	moves=0

	current_state = initial_state.copy()
	while moves<20:
		current_state, tabu, moves = change_two_bits(current_state, tabu, moves)
		print("Current state: " , current_state)
		print("Tabu: ", tabu)
		print()
		if current_state==final_state:
			# print("Goal state reached in ", moves, " moves")
			break
		sleep(2)
	if moves==20:
		print("Tabu Tenure: Changing to one bit")
	while current_state!=final_state:
		current_state, tabu, moves = change_one_bit(current_state, tabu, moves)
		print("Current state: " , current_state)
		print("Tabu: ", tabu)
		print()
		sleep(2)
	print("Goal state reached in ", moves, " moves")


if __name__ == '__main__':
	initial_state, final_state = get_states()
	tabu(initial_state, final_state)