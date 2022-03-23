def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed and st < len(a) and ed < len(a)):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i])
    return

test_cases = 1
for cs in range (test_cases):
    n = 7
    a = [1, 2, 3, 4, 5, 6, 7]
    findZigZagSequence(a, n)



