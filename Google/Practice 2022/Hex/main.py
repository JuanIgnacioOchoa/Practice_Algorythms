from copy import deepcopy
from sys import stdin, stdout
import os
import time
start_time = time.time()
"""
Problem
Download the Starter Code!
This problem was inspired by a board game called Hex, designed independently by Piet Hein and John Nash. It has a similar idea, but does not assume you have played Hex.

This game is played on an N×N board, where each cell is a hexagon. There are two players: Red side (using red stones) and Blue side (using blue stones). The board starts empty, and the two players take turns placing a stone of their color on a single cell within the overall playing board. Each player can place their stone on any cell not occupied by another stone of any color. There is no requirement that a stone must be placed beside another stone of the same color. The player to start first is determined randomly (with equal probability among the two players).

The upper side and lower sides of the board are marked as red, and the other two sides are marked as blue. For each player, the goal of the game is to connect the two sides marked with their color by forming a connected path using stones of their color. The first player to achieve this wins. Note that the four corners are considered connected to both colors.

The game ends immediately when one player wins.

Given a game state, help someone new to the game determine the status of a game board. Say one of the following:

Impossible: If it was impossible for two players to follow the rules and to have arrived at that game state.
Red wins: If the player playing the red stones has won.
Blue wins: If the player playing the blue stones has won.
Nobody wins: If nobody has yet won the game. Note that a game of Hex cannot end without a winner!
Note that in any impossible state, the only correct answer is Impossible, even if red or blue has formed a connected path of stones linking the opposing sides of the board marked by their colors.

Here is a an example game on a 6×6 gameboard where blue won. Blue was the first player to move, and placed a blue stone at cell marked as 1. Then Red placed at cell 2, then blue at cell 3, etc. After the 11-th stone is placed, blue wins.


Input
The first line of input gives the number of test cases, T. T test cases follow. Each test case start with the size of the side of the board, N. This is followed by a board of N rows and N columns consisting of only B, R, and . characters. B indicates a cell occupied by blue stone, R indicates a cell occupied by red stone, and . indicates an empty cell.

Output
For each test case, output one line containing Case #x: y, where x is the case number (starting from 1) and y is the status of the game board. It can be "Impossible", "Blue wins", "Red wins", or "Nobody wins" (excluding the quotes). Note that the judge is case-sensitive, so answers of "impossible", "blue wins", "red wins", and "nobody wins" will be judged incorrect.

Limits
Time limit: 30 seconds.
Memory limit: 1 GB.
1≤T≤100.
Test Set 1
1≤N≤10.
Test Set 2
1≤N≤100.
"""
class Node():
    def __init__(self, h, key = None, position = None, parent = None):
        self.parent = parent
        self.value = h
        self.position = position
        self.key = key
    def __eq__(self, other):
        return self.position == other.position
def insert(open, node):
    i = 0
    j = len(open)- 1
    if len(open) == 0 or node.value < open[0].value:
        open.insert(0, node)
        return
    elif node.value > open[-1].value:
        open.append(node)
        return
    while i < j:
        if open[i].value > node.value:
            open.insert(i, node)
            return
        if open[j].value < node.value:
            open.insert(j+1, node)
            return   

        i+=1
        j-=1
    open.insert(i, node)
def getKey(position):
    return (str(position[0])+"-"+str(position[1]))
def dijkstra(position, n, second = 0):
    nodes = {}
    start = Node(0, -1, [-1, -1])
    end = Node(float('inf'), n, [n, n])
    for key in position:
        for p in position[key]:
            tmp = Node(float('inf'), key, p)
            nodes[getKey(p)] = tmp
    open = [start]
    closed = []
    winningNodes = []
    while len(open):
        current = open[0]
        pos = current.position
        if current == start:
            posibilities = []
            for i in range(n):
                posibilities.append([0, i])
        elif current.position[0] + 1 == n:
            tmpNode = end
            val = 1
            if tmpNode.value == float('inf') or tmpNode.value > current.value + val:
                tmpNode.value = current.value + val
                tmpNode.parent = current
            if current not in winningNodes:
                winningNodes.append(current)
            closed.append(open.pop(0))
            continue
        else :
            posibilities = [
                [pos[0]-1, pos[1]],
                [pos[0]-1, pos[1]+1],
                [pos[0], pos[1]+1],
                [pos[0]+1, pos[1]],
                [pos[0]+1, pos[1]-1],
                [pos[0], pos[1]-1],
            ]
        for posib in posibilities:
            tmpKey = getKey(posib)
            if tmpKey in nodes:
                tmpNode = nodes[tmpKey]
                val = 4 if abs(posib[0] - pos[0]) == 1 and abs(posib[1] - pos[1]) == 1 else 1
                if tmpNode.value == float('inf') or tmpNode.value > current.value + val:
                    tmpNode.value = current.value + val
                    tmpNode.parent = current
                if tmpNode not in open and tmpNode not in closed:
                    insert(open, tmpNode)
            
        closed.append(open.pop(0))

    if len(winningNodes) > 1:
        tmp1 = winningNodes[0]
        tmp2 = winningNodes[1]
        pos2 = deepcopy(position)
        while tmp1.parent:
            position[tmp1.key].remove(tmp1.position)
            tmp1 = tmp1.parent
            
        while tmp2.parent:
            pos2[tmp2.key].remove(tmp2.position)
            tmp2 = tmp2.parent
        if dijkstra(position, n) or dijkstra(pos2, n):
            return -1
        return True
    elif len(winningNodes) == 1:
        return True
    return False     
def getWinner(board):
    n = len(board)
    tBlues = {}
    tReds = {}
    blues = 0
    reds = 0
    blankSpaces = 0
    i = 0
    while i < n:
        j = 0
        vertical = True
        horizontal = True
        while j < n:
            if board[i][j] == "R":
                reds+=1
                if i not in tReds:
                    tReds[i] = []
                tReds[i].append([i, j])
            elif board[i][j] == "B":
                blues+=1
                if j not in tBlues:
                    tBlues[j] = []
                tBlues[j].append([j, i])
            else:
                blankSpaces+=1
            j+=1
        
        i+=1
    
    if abs(blues - reds) >= 2 :
        winner = 'Impossible'
    else:
        red = dijkstra(tReds, n)
        blue = dijkstra(tBlues, n)
        #astar(tBlues, n)
        #blue = isWinner(tBlues, n)
        #red = isWinner(tReds, n)
        if (blue == -1 or red == -1) or (blue and red):
            winner = "Impossible"
        elif blue:
            if reds > blues:
                winner = "Impossible"
            else:
                winner = 'Blue wins'
        elif red:
            if blues > reds:
                winner = "Impossible"
            else:
                winner = "Red wins"
        else:
            winner = "Nobody wins"
    return winner



def floodfill(board, color, x, y, n, visited):
    if [x, y] in visited:
        return False
    visited.append([x, y])
    if y == n - 1:
        return True
    x1 = False
    x2 = False
    x3 = False
    x4 = False
    x5 = False
    x6 = False
    if x > 0 and y < n - 1:
        if board[x-1][y+1] == color:
            x1 = floodfill(board, color, x - 1, y + 1, n, visited)
    if y > 0 and x < n - 1:
        if board[x+1][y-1] == color:
            x2 = floodfill(board, color, x + 1, y - 1, n, visited)
    if x > 0:
        if board[x-1][y] == color:
            x3 = floodfill(board, color, x - 1, y, n, visited)
    if y > 0:
        if board[x][y-1] == color:
            x4 = floodfill(board, color, x, y - 1, n, visited)
    if x < n - 1:
        if board[x+1][y] == color:
            x5 = floodfill(board, color, x + 1, y, n, visited)
    if y < n - 1:
        if board[x][y+1] == color:
            x6 = floodfill(board, color, x, y + 1, n, visited)
    return x1 or x2 or x3 or x4 or x5 or x6
def findWinner(board):
    blues = 0
    reds = 0
    n = len(board)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if board[i][j] == 'B':
                blues += 1
            elif board[i][j] == 'R':
                reds += 1
            j+=1
        i+=1
    if abs(reds - blues) >= 2 :
        return "Impossible"
    i = 0
    visited = []
    blue = False
    red = False
    while i < n:
        if board[i][0] == 'B':
            blue = floodfill(board, 'B', i, 0, n, visited)
            if blue:
                break
        i+=1
    tmp = True
    c = 0

    if blue:
        i = 0
        while i < n:
            j = 0
            while j < n:
                if board[i][j] == 'B':
                    board[i][j] = '.'
                    y = False
                    k = 0
                    while k < n:
                        if board[k][0] == 'B':
                            c = 1
                            tmp = tmp and not floodfill(board, 'B', 0, k, n, [])
                            if tmp:
                                board[i][j] = "B"
                                i = n
                                j = n
                                k = n
                                break
                        k+=1
                    if i < n and j < n:
                        board[i][j] = "B"
                j += 1
            i += 1
                    
                        
    if not tmp or (c == 0 and blue):
        if reds > blues:
            return 'Impossible'
        else:
            return 'Blue wins'
    elif blue:
        return 'Impossible'
    
    visited = []
    red_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0])-1,-1,-1)]
    i = 0
    while i < n:
        if board[0][i] == 'R':
            red = floodfill(red_board, 'R', 0, i, n, visited)
            if red:
                break
        i+=1
    
    tmp = True
    if red:
        for i in range(n):
            for j in range(n):
                if red_board[i][j] == 'R':
                    red_board[i][j] = '.'
                    y = False
                    for k in range(n):
                        if red_board[k][0] == 'R':
                            tmp = tmp and floodfill(red_board, 'R', 0, k, n, [])
                    red_board[i][j] = "R"
                    
                        
    if not tmp:
        if blues > reds:
            return 'Impossible'
        else:
            return 'Red wins'
    elif red:
        return 'Impossible'
    
    return 'Nobody wins'
dir = os.path.dirname(__file__)
inp = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())


for case in range(t):
    n = int(inp.readline().strip())
    board = []
    for i in range(n):
        board.append(list(inp.readline().strip()))

    winner = findWinner(board)
    #winner = getWinner(board)
    result = (out.readline().split(':')[1]).strip()
    if winner != result:
        ans =('Case #%d: Error Wrong: %s, correct: %s') % (case+1, winner, result)
    else:
        ans =('Case #%d: %s') % (case+1, winner)
    
    print(ans)

print("--- %s seconds ---" % (time.time() - start_time))