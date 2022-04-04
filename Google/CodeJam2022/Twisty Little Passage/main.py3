
from sys import stdin, stdout
import math
import random

def main():
    t = int(input())
    #t = 100        
    # 

    for case in range(t):

        N, K = map(int, input().split())
        #N, K = map(int, raw_input().split())
        operations = 0
        action = ''
        randomlist = random.sample(range(1, N + 1), min(N, K))
        passageList = []
        visited = []
        while operations < K - 1:
            room, passages = map(int, input().split())
            #room, passages = map(int, raw_input().split())
            if operations == 0:
                action = "W"
            elif len(randomlist) == 0:
                break
                action = "W"
            elif operations % 2 == 0 and room not in visited:
                action = "W"
            else:
                nextRoom = randomlist.pop()
                while nextRoom in visited and len(randomlist) > 0:
                    nextRoom = randomlist.pop()
                action = "T " + str(nextRoom)

            if room not in visited:
                passageList.append(passages)
                visited.append(room)

            print(action)
            operations += 1
        total = sum(passageList)
        mean = 1
        if len(passageList) != 0:

            mean = float(float(total) / float(len(passageList)))
        ans = int(((mean * N) / 2) + (mean / 2))
        t1 = (mean*(N)) / 2
        print('E ' + str(int(ans)))
        #input()
main()