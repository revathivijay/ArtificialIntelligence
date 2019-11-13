import math

max_level = 10

def nCr(n, r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def nPr(n, r):
    return math.factorial(n)/math.factorial(n-r)

def calculate():
    CompMove = [0]*max_level
    userMove = [0]*max_level
    moves_left = [0]*max_level
    NL = [0]*max_level
    NVS = [0]*max_level
    NIS = [0]*max_level
    NL[0] = 1

    for i in range(9, 0, -1):
        print (i)
        if (i%2==0):
            CompMove[max_level-i] = CompMove[max_level-i-1]
            userMove[max_level-i] = userMove[max_level-i-1]+1
        else:
            CompMove[max_level - i] = CompMove[max_level - i - 1] + 1
            userMove[max_level - i] = userMove[max_level - i - 1]

        moves_left[max_level-i] = i
        NL[max_level-i] = i*NL[max_level-i-1]

    for i in range(0, 10):
        print(i)
        if(i<6):
            NVS[i] = NL[i]
            NIS[i] = 0

        else:
            child_invalid_state =0
            intersection = 0
            level_invalid_state = 8*nPr(3,3)*nCr(6, (i-3))*nPr(i-3, i-3)
            if(i>=8):
                level_invalid_state*=nCr(3,2)
            if(i>6):
                intersection=(2*nCr(3,2)*nPr(3,3)*nPr(3,3)*nCr(3, i-6)*nPr(i-6, i-6))
                child_invalid_state = NIS[i-1]*moves_left[i]
                cl = CompMove[i]
                ul = userMove[i]
                if(i%2==0):
                    ul-=1
                else:
                    cl-=1

                if i>7:
                    intersection *= nCr(cl, 3)
                if i>8:
                    intersection*=nCr(ul, 3)

            NIS[i] = level_invalid_state + child_invalid_state - intersection
            #print(intersection)

    for i in range(max_level):
        print("Level no: ", i)
        print("No of invalid States: ", NIS[i])
        print()

calculate()