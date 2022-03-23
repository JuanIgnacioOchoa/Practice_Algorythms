

from sys import stdin, stdout
import os
import time
start_time = time.time()

def queensAttack(n, k, r_q, c_q, obstacles):
    ans = 0
    possibleAttacks = (n-1) * 2
    possibleAttacks += min(n - r_q, n - c_q)
    possibleAttacks += min(n - r_q, c_q - 1)
    possibleAttacks += min(r_q - 1, n - c_q)
    possibleAttacks += min(r_q-1, c_q-1)
    if len(obstacles) == 0:
        return possibleAttacks
    rowsObst = [[],[],[],[],[],[],[],[]]
    for row, col in obstacles:
        if r_q == row:
            if col < c_q:
                if len(rowsObst[4]) == 0:
                    rowsObst[4].append([row, col])
                else:
                    tmp = rowsObst[4][1]
                    if abs(col - c_q) < abs(tmp - c_q):
                        rowsObst[4].pop()
                        rowsObst[4].append([row, col])
            else:
                if len(rowsObst[5]) == 0:
                    rowsObst[5].append([row, col])
                else:
                    tmp = rowsObst[5][1]
                    if abs(col - c_q) < abs(tmp - c_q):
                        rowsObst[5].pop()
                        rowsObst[5].append([row, col])
                #possibleAttacks -= n - col
        elif c_q == col:
            if row < r_q:
                if len(rowsObst[6]) == 0:
                    rowsObst[6].append([row, col])
                else:
                    tmp = rowsObst[6][0]
                    if abs(col - c_q) < abs(tmp - c_q):
                        rowsObst[6].pop()
                        rowsObst[6].append([row, col])
                #possibleAttacks -= row
            else:
                if len(rowsObst[7]) == 0:
                    rowsObst[7].append([row, col])
                else:
                    tmp = rowsObst[7][0]
                    if abs(col - c_q) < abs(tmp - c_q):
                        rowsObst[7].pop()
                        rowsObst[7].append([row, col])
                #possibleAttacks -= n - row
        else:
            d_row = (row - r_q)
            d_col = (col - c_q)
            if abs(d_col) == abs(d_row):
                if d_col < 0 and d_row < 0:
                    # DL
                    if len(rowsObst[0]) == 0:
                        rowsObst[0].append([row, col])
                    else:
                        tmp = rowsObst[0][0]
                        if abs(tmp[0] - r_q) > abs(d_col):
                            rowsObst[0].pop()
                            rowsObst[0].append([row, col])
                    #possibleAttacks -= min(row, col)
                elif d_col > 0 and d_row > 0:
                    #UR
                    if len(rowsObst[1]) == 0:
                        rowsObst[1].append([row, col])
                    else:
                        tmp = rowsObst[1][0]
                        if abs(tmp[0] - r_q) > abs(d_col):
                            rowsObst[1].pop()
                            rowsObst[1].append([row, col])
                    #possibleAttacks -= (min(n - row, n - col)) + 1
                elif d_col < 0 and d_row > 0:
                    #UL
                    if len(rowsObst[2]) == 0:
                        rowsObst[2].append([row, col])
                    else:
                        tmp = rowsObst[2][0]
                        if abs(tmp[0] - r_q) > abs(d_col):
                            rowsObst[2].pop()
                            rowsObst[2].append([row, col])
                    #possibleAttacks -= (min(n - row, col)) + 1  
                elif d_col > 0 and d_row < 0:
                    #DR
                    if len(rowsObst[3]) == 0:
                        rowsObst[3].append([row, col])
                    else:
                        tmp = rowsObst[3][0]
                        if abs(tmp[0] - r_q) > abs(d_col):
                            rowsObst[3].pop()
                            rowsObst[3].append([row, col])
                    #possibleAttacks -= (min(row, n - col)) + 1

    for i in range(len(rowsObst)):
        if len(rowsObst[i]) <= 0:
            if i == 0:
                print(9)
                #DL
                ans += min(r_q, c_q) - 1
            elif i == 1:
                #UR
                ans += min(n - r_q, n - c_q)
            elif i == 2:
                #UL
                ans += min(n - r_q, c_q - 1)
            elif i == 3:
                #DR
                ans += min(r_q - 1, n - c_q)
            elif i == 4:
                #Down
                ans += c_q - 1
            elif i == 5:
                #UP
                ans += n - c_q
            elif i == 6:
                #IZQ
                ans += r_q - 1
            elif i == 7:
                #DER
                ans += n - r_q
            continue
        row = rowsObst[i][0][0]
        col = rowsObst[i][0][1]
        d_row = (row - r_q)
        d_col = (col - c_q)
        if r_q == row:
            ans += abs(col - c_q) - 1
        elif c_q == col:
            ans += abs(row - r_q) - 1
        else :
            ans += abs(d_row) - 1
        #elif d_col < 0 and d_row < 0:
        #    possibleAttacks -= min(row, col)
        #elif d_col > 0 and d_row > 0:
        #    possibleAttacks -= (min(n - row, n - col)) + 1
        #elif d_col < 0 and d_row > 0:
        #    possibleAttacks -= (min(n - row, col)) + 1  
        #elif d_col > 0 and d_row < 0:
        #    possibleAttacks -= (min(row, n - col)) + 1
    #ans = possibleAttacks
    return ans

dir = os.path.dirname(__file__)
inp = open(os.path.join(dir, 'input.txt'),'r')

first_multiple_input = inp.readline().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

second_multiple_input = inp.readline().rstrip().split()

r_q = int(second_multiple_input[0])

c_q = int(second_multiple_input[1])

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, inp.readline().rstrip().split())))

result = queensAttack(n, k, r_q, c_q, obstacles)

print("--- %s seconds ---" % (time.time() - start_time))