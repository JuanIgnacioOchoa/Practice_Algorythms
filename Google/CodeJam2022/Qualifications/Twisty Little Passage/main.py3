
import sys 
import random

def main():
    t = int(input())
    #t = 100        
    # 

    for case in range(t):
        sample = {}
        known = {}
        N, K = map(int, input().split())
        #N, K = map(int, raw_input().split())
        operations = 0
        action = ''
        randomlist = random.sample(range(1, N + 1), min(N, K))
        room, passages = map(int, input().split())
        sample[room] = passages
        while operations < K:
            print('W')

            room, passages = map(int, input().split())
            known[room] = passages
            if len(randomlist) > 1:
                nxt = randomlist.pop()
                while (nxt in sample or nxt in known) and len(randomlist) > 1:
                    nxt = randomlist.pop()

                print("T {}".format(nxt))
                room, passages = map(int, input().split())

                sample[room] = passages
            else:
                print('W')

                room, passages = map(int, input().split())
                known[room] = passages
            operations += 2
        knownSum = 0
        sampleSum = 0
        for key in known:
            if key in sample: 
                continue
            knownSum += known[key]
        for key in sample:
            sampleSum += sample[key]
        mean = float(sampleSum) / float(len(sample))
        estimated = (mean * N + knownSum) / 2
        print('E ' + str(int(estimated)))
        #input()
main()