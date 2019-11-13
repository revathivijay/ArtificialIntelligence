import numpy as np

# Initial values of Aplha and Beta 
MAX, MIN = 10000, -10000

# Returns optimal value for current player 
#(Initially called for root and maximizer) 
def minimax(depth, nodeIndex, maximizingPlayer, 
            values, alpha, beta, height): 

    # Terminating condition. i.e 
    # leaf node is reached 
    if depth == 3: 
        return values[nodeIndex] 

    if maximizingPlayer: 
    
        best = MIN

        # Recur for left and right children 
        for i in range(0, 2): 
            
            val = minimax(depth + 1, nodeIndex * 2 + i, 
                        False, values, alpha, beta, height) 
            best = max(best, val) 
            alpha = max(alpha, best) 
            print("Maximizing node")
            print("Depth: ", depth)
            print("Changing alpha to: ", alpha)
            print("Beta: ", beta)
            print()
            # Alpha Beta Pruning

            if beta <= alpha:
                print("ALPHA CUTOFF")
                break
        
        return best 
    
    else: 
        best = MAX

        # Recur for left and 
        # right children 
        for i in range(0, 2): 
        
            val = minimax(depth + 1, nodeIndex * 2 + i, 
                            True, values, alpha, beta, height) 
            best = min(best, val) 
            beta = min(beta, best) 

            print("Minimizing node")
            print("Depth: ", depth)
            print("Changing beta to: ", beta)
            print("Alpha: ", alpha)
            print()
            # Alpha Beta Pruning 
            if beta <= alpha: 
                print("BETA CUTOFF")
                break
        
        return best 
    
# Driver Code 
if __name__ == "__main__": 

    values = [3, 5, 6, 9, 1, 2, 0, -1]
    height = np.log(len(values))/np.log(2) 
    print("Leaf Nodes: ", values)
    print("Height of tree: ", height)
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX, height)) 
    
# This code is contributed by Rituraj Jain 
