import random


t = int(input())
highLimit = (10**9) + 1
for case in range(t):
    N = int(input())
    #N = 100
    power = 1
    i = 1
    lst1 = []
    while power < highLimit and i < N:
        lst1.append(power)
        power = 2**i
        i+=1
    while i <= N:
        filler = random.randint(1, highLimit)
        while filler in lst1:
            filler = random.randint(1, highLimit)
        lst1.append(filler)
        i+=1
    strings = [str(x) for x in lst1]
    print(" ".join(strings))
    lst2 = list(map(int, input().split(' ')))
    lst = lst1 + lst2
    lst.sort()
    j = len(lst) - 1
    curr = 0
    target = int(sum(lst) / 2)
    ans = []
    while j >= 0 and curr != target:
        if curr + lst[j] <= target:
            curr += lst[j]
            ans.append(lst[j])
        j -= 1
    ans = [str(x) for x in ans]
    print(" ".join(ans))