def alternate(children, j, h):
    for i in children:
        mini = 1000
        temp = []
        if isinstance(i, tuple):
            heu = h[i[0]] + h[i[1]] + 20
            if mini >= h[i[0]] + h[i[1]] + 20:
                temp.append(i)
                mini = h[i[0]] + h[i[1]] + 20
        else:
            heu = h[i]
            if mini >= h[i] + 10:
                temp.append(i)
                mini = h[i] + 10
        return temp[-2]


def marksolve(solve,open):
    for i in open:
        if isinstance(i,tuple):
            for j in graph[i[0]]:
                if isinstance(j,tuple):
                    if solve[j[0]] and solve[j[1]] and j in open:
                        solve[i[0]] = True
                        break
                else:
                    if solve[j] and j in open:
                        solve[i[0]] = True
                        break
            for j in graph[i[1]]:
                if isinstance(j,tuple):
                    if solve[j[0]] and solve[j[1]] and j in open:
                        solve[i[1]] = True
                        break
                else:
                    if solve[j] and j in open:
                        solve[i[1]] = True
                        break
        else:
            for j in graph[i]:
                if isinstance(j,tuple):
                    if solve[j[0]] and solve[j[1]] and j in open:
                        solve[i] = True
                        break
                else:
                    if solve[j] and j in open:
                        solve[i] = True
                        break

def getkey(i, open, graph):
    for c in open:
        if isinstance(c, tuple):
            for j in graph[c[0]]:
                if isinstance(j, tuple):
                    if i == j[0] or i == j[1]:
                        return c[0]
                else:
                    if i == j:
                        return c[0]
            for j in graph[c[1]]:
                if isinstance(j, tuple):
                    if i == j[0] or i == j[1]:
                        return c[1]
                else:
                    if i == j:
                        return c[1]
        else:
            for j in graph[c]:
                if isinstance(j, tuple):
                    if i == j[0] or i == j[1]:
                        return c
                else:
                    if i == j:
                        return c


def aostar(graph, h):
    faltu = 20
    solve = {}
    for i in graph:
        if i not in solve:
            solve[i] = False
    solve["CLOSED"] = True
    te = 0
    flag = 0
    start = "A"
    open = [start]
    alt = [start]
    futility = 1000
    while not solve[start] and h[start] <= futility:
        faltu -=1
        if faltu<0:
            break

        if isinstance(open[-1], tuple):
            z = open[-1]
            te = 0

            for j in [1,0]:
                n = z[j]

                children = []
                for i in graph[n]:
                    children.append(i)
                mini = 1000
                temp = []
                for i in children:
                    if isinstance(i, tuple):
                        heu = h[i[0]] + h[i[1]] + 20
                        if mini >= h[i[0]] + h[i[1]] + 20:
                            temp.append(i)
                            mini = h[i[0]] + h[i[1]] + 20
                    else:
                        heu = h[i]
                        if mini >= h[i] + 10:
                            temp.append(i)
                            mini = h[i] + 10

                if temp[-1] not in open:
                    open.append(temp[-1])
                # if isinstance(open[-1], tuple):
                #     if open[-1][0] == "CLOSED" and open[-1][1] == "CLOSED":
                #         open.pop()
                #         solve[open[-1]] = True
                # else:
                #     if open[-1] == "CLOSED":
                #         open.pop()
                #         solve[open[-1]] = True
                if flag == 0:
                    if isinstance(temp[-2], tuple):
                        tee = h[temp[-2][0]] + h[temp[-2][1]] + 20
                    else:
                        tee = h[temp[-2]] + 10
                    alt.append(temp[-2])
                    flag = 1

                for c in open[::-1]:
                    a = start
                    if isinstance(c, tuple):
                        heu = h[c[0]] + h[c[1]] + 20
                        if c in graph[n]:
                            a = n
                            if c == "CLOSED" or c == ("CLOSED","CLOSED"):
                                solve[n] = True
                        else:
                            a = getkey(c[0], reversed(open[:-1]), graph)
                        h[a] = heu

                    else:
                        heu = h[c] + 10
                        if c in graph[n]:
                            a = n
                            if c == "CLOSED" or c == ("CLOSED","CLOSED"):
                                solve[n] = True
                        else:
                            a = getkey(c, reversed(open[:-1]), graph)
                        h[a] = heu

                    if a == start:
                        break
                marksolve(solve,open)
                print(open)
                open = checksolve(open, graph, solve,h)

                if h[start] > tee:
                    temp[:] = open[:2]
                    open[:] = alt[:]
                    alt[:] = temp[:]
                    tee = h[start]
                    te = 1
                if te ==1:
                    break


        else:
            children = []
            n = open[-1]

            for i in graph[n]:
                children.append(i)
            mini = 1000
            temp = []
            for i in children:
                if isinstance(i, tuple):
                    heu = h[i[0]] + h[i[1]] + 20

                    if mini >= h[i[0]] + h[i[1]] + 20:
                        temp.append(i)

                        mini = h[i[0]] + h[i[1]] + 20
                else:
                    heu = h[i]
                    if mini >= h[i] + 10:
                        temp.append(i)
                        mini = h[i] + 10

            open.append(temp[-1])
            # if isinstance(open[-1], tuple):
            #     if open[-1][0] == "CLOSED" and open[-1][1] == "CLOSED":
            #         open.pop()
            #         solve[open[-1]] = True
            # else:
            #     if open[-1] == "CLOSED":
            #         open.pop()
            #         solve[open[-1]] = True
            if flag == 0:
                if isinstance(temp[-2], tuple):
                    tee = h[temp[-2][0]] + h[temp[-2][1]] + 20
                else:
                    tee = h[temp[-2]] + 10
                alt.append(temp[-2])
                flag = 1

            for c in open[::-1]:
                if isinstance(c, tuple):
                    heu = h[c[0]] + h[c[1]] + 20
                    if c in graph[n]:
                        a = n
                        if c == "CLOSED" or c == ("CLOSED", "CLOSED"):
                            solve[n] = True
                    else:
                        a = getkey(c[0], reversed(open[:-1]), graph)
                    h[a] = heu

                else:
                    heu = h[c] + 10
                    if c in graph[n]:
                        a = n
                        if c == "CLOSED" or c == ("CLOSED", "CLOSED"):
                            solve[n] = True
                    else:
                        a = getkey(c, reversed(open[:-1]), graph)
                    h[a] = heu

                if a == start:
                    break
            print(open)
            open = checksolve(open, graph, solve, h)

            if h[start] >= tee:
                temp[:] = open[:2]
                open[:] = alt[:]
                alt[:] = temp[:]
                tee = h[start]


            marksolve(solve,open)
    if solve[start]:
        print(h[start])


def checksolve(open, graph, solve,h):
    for i in open[::-1]:
        if i == "CLOSED" :
            a = getkey(i, reversed(open[:-1]), graph)
            solve[a] = True
            h[a]=10
            open.pop()
            return open
        elif i == ("CLOSED", "CLOSED"):
            a = getkey(i[0], reversed(open[:-1]), graph)
            solve[a] = True
            h[a] = 20
            open.pop()
            return open

        return open
        # else:
        #
        #     solvevalue = False
        #     if isinstance(i,tuple):
        #         for j in graph[i[0]]:
        #             if j in open and solve[j]:
        #                 solvevalue = True
        #
        #             elif j in open and not solve[j]:
        #                 solvevalue = False
        #         solve[i[0]] = solvevalue
        #         for j in graph[i[1]]:
        #             if j in open and solve[j]:
        #                 solvevalue = True
        #
        #             elif j in open and not solve[j]:
        #                 solvevalue = False
        #         solve[i[1]] = solvevalue
        #
        #     else:
        #         if graph[i]:
        #             for j in graph[i]:
        #                 if j in open and solve[j]:
        #                     solvevalue = True
        #                     open.pop()
        #                 elif j in open and not solve[j]:
        #                     solvevalue = False
        #             solve[i] = solvevalue
        #     return open

if __name__ == "__main__":
    graph = {
        "A": [("B", "C"), ("D", "E")],
        "B": [("F", "G"), "CLOSED"],
        "C": [("H", "I")],
        "D": [("H", "I"), "J"],
        "E": ["K", ("CLOSED", "CLOSED")],
        "F": ["CLOSED", "CLOSED"],
        "G": ["CLOSED"],
        "H": ["CLOSED"],
        "I": ["CLOSED"],
        "J": ["K", "L", "M"],
        "M": ["CLOSED"],
        "K": ["CLOSED"],
        "L": ["M", "CLOSED"],
        "CLOSED": []
    }

    print("Graph: ", graph)
    print()
    heuristic = {
        "A": 21,
        "B": 6,
        "C": 7,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 8,
        "H": 3,
        "I": 4,
        "J": 7,
        "K": 10,
        "L": 9,
        "M": 10,
        "CLOSED": 0
    }
    print("Heuristics: ", heuristic)
    print()
    aostar(graph, heuristic)