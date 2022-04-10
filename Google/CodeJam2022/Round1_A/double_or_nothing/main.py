from sys import stdin, stdout
import os
import time


start_time = time.time()


def getWord(word):
    ans = ""
    i = 0
    while i < len(word) - 1:
        if word[i] < word[i+1]:
            ans += word[i] + word[i]
        elif word[i] == word[i+1]:
            c = 1
            while i < len(word) - 1 and word[i] == word[i+1]:
                i += 1
                c += 1
            if i == len(word) - 1:
                st = i - c + 1
                ans += word[st: i]
            else:
                if word[i] < word[i+1]:
                    ans += word[i] * (c * 2)
                else:
                    ans += word[i] * (c)
        else:
            ans += word[i]
        i+=1
    ans += word[-1]
    return ans
dir = os.path.dirname(__file__)


stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    word = stdin.readline().strip()

    tmpans = getWord(word)
    res = stdout.readline().strip()
    ans = (('Case #%d: %s') % (case+1, tmpans))
    if res != ans:
        print('Error ' + res)
        print(ans)
    else: 
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))