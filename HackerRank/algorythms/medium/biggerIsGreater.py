def biggerIsGreater(S):
    i = 0
    ans = 0
    while i < len(S) - 1:
        j = i + 1
        while j < len(S):
            if S[i] > S[j]:
                tmp = list(S)
                tmp[i], tmp[j] = tmp[j], tmp[i]
                tmp = ''.join(tmp)
                if ans == 0 or ans > tmp:
                    ans = tmp
            j+=1
        i+= 1
    if ans == 0:
        return 'no answer'
    else:
        return ans

biggerIsGreater('dkhc')