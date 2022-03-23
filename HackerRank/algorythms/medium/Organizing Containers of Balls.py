

from sys import stdin, stdout
import os
import time
start_time = time.time()

def organizingContainers(container):
    ans = 'Impossible'

    containerSize = [sum(x) for x in container]
    ballsAmnt = [sum(x) for x in zip(*container)]
    i = 0
    tmpLen = 0
    while i < len(containerSize) and tmpLen != len(containerSize):
        tmpLen = len(containerSize)
        j = 0
        while j < len(ballsAmnt):
            if containerSize[i] == ballsAmnt[j]:
                containerSize.pop(i)
                ballsAmnt.pop(j)
                i-=1
                break
            j+=1
        i+=1
    if len(containerSize) != 0:
        return ans
    
    return "Possible"

dir = os.path.dirname(__file__)
inp = open(os.path.join(dir, 'input.txt'),'r')

q = int(inp.readline())


for q_itr in range(q):
    
    n = int(inp.readline().strip())

    container = []

    for _ in range(n):
        container.append(list(map(int, inp.readline().rstrip().split())))

    result = organizingContainers(container)
print("--- %s seconds ---" % (time.time() - start_time))