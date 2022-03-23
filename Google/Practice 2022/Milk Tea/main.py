from sys import stdin, stdout
import os
import time
start_time = time.time()
"""
Problem
Download the Starter Code!
The milk tea in China is very delicious. There are many binary ("either-or") options for customizing a milk tea order, such as:

"with ice" OR "no ice"
"with sugar" OR "no sugar"
"with bubbles" OR "no bubbles"
"with pudding" OR "no pudding"
and so on.
A customer's preferences for their milk tea can be represented as a binary string. For example, using the four properties above (in the order they are given), the string 1100 means "with ice, with sugar, no bubbles, no pudding".

Today, Shakti is on duty to buy each of his N friends a milk tea, at a shop that offers P binary options. But after collecting everyone's preferences, Shakti found that the order was getting too complicated, so Shakti has decided to buy the same type of milk tea for everyone. Shakti knows that for every friend, for every preference that is not satisfied, they will complain once. For example, if two of the friends have preferences for types 101 and 010, and Shakti chooses type 001, then the first friend will complain once and the second friend will complain twice, for a total of three complaints.

Moreover, there are M different forbidden types of milk tea that the shop will not make, and Shakti cannot choose any of those forbidden types.

What is the smallest number of complaints that Shakti can get?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing 3 integers N, M, and P, as described above. Then, there are N more lines, each of which contains a binary string; these represent the preferences of the N friends. Finally, there are M more lines, each of which contains a binary string; these represent the forbidden types of milk tea that the shop will not make. Binary strings consist only of 0 and/or 1 characters.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of complaints that Shakti can get, per the rules described above.

Limits
Time limit: 30 seconds.
Memory limit: 1 GB.
1≤T≤100.
All of the forbidden types of milk tea are different.
Test Set 1
1≤N≤10.
1≤M≤min(10,2P−1).
1≤P≤10.
Test Set 2
1≤N≤100.
1≤M≤min(100,2P−1).
1≤P≤100.
"""
def insert(lst, tple):
    i = 0
    j = len(lst)- 1
    if len(lst) == 0 or tple[1] <= lst[0][1]:
        lst.insert(0, tple)
        return
    elif tple[1] > lst[-1][1]:
        lst.append(tple)
        return
    while i < j:
        if lst[i][1] > tple[1]:
            lst.insert(i, tple)
            return
        if lst[j][1] < tple[1]:
            lst.insert(j+1, tple)
            return   

        i+=1
        j-=1
    if lst[i][1] > tple[1]:
        lst.insert(i, tple)
    else:
        lst.insert(i+1, tple)
    return

def convertLsttoStr(lst):
    ans = ""
    for l in lst:
        ans+=str(l)
    return ans

def getComplaints(preferences, forbiddens, P):
    ans = float('inf')
    dp = {}
    current = "0" * P
    end = "1" + current
    cnt = 0
    while current != end:
        if current in forbiddens:
            cnt+=1
            current = str(bin(cnt))[2:]
            current = "0" * (P - len(current)) + current
            continue
        tmpCom = 0
        for i in range(P):
            if tmpCom > ans:
                break
            key = str(i)+"-"+current[i]
            tmpKey = 0
            if key not in dp:
                for pref in preferences:
                    if pref[i] != current[i]:
                        tmpKey += 1
                dp[key] = tmpKey
                tmpCom += tmpKey
            else:
                tmpCom = dp[key]
        if ans > tmpCom:
            ans = tmpCom
        cnt+=1
        current = str(bin(cnt))[2:]
        current = "0" * (P - len(current)) + current
        
    return ans

    
def getComplaints2(preferences, forbiddens, P):
    ans = float('inf')
    current = "0" * P
    end = "1" + current
    cnt = 0
    lst = []

    for i in range(P):
        cnt = 0
        for pref in preferences:
            cnt += int(pref[i])
        tple = (i, cnt)
        insert(lst,tple)
    i = 0
    j = P - 1
    val = [-1] * P
    n = len(preferences)
    n2 = float((n)/2.0)
    complaints = []
    ans = 0
    while i < j:
        back = lst[j][1]
        front = lst[i][1]
        if ((n) - front) < n2:
            insert(complaints, [i, n - front])
            val[j] = "1"
        else:
            val[j] = "0"
            insert(complaints, [i , front])
        if ((n) - back) < n2:
            complaints.append([j, n - back])
            val[i] = "1"
        else: 
            complaints.append([j, back])
            val[i] = "0"
        i+=1
        j-=1
    main = convertLsttoStr(val)
    s = main
    current = None
    visited = [convertLsttoStr(val)]
    locked = []
    stack = []
    k = 1
    while s in forbiddens:
        h = 0
        tmp = []
        while h < k:
            tmp.append(complaints.pop())
            h+=1
        h = 0
        while h < k:
            
            val[tmp[h][0]] = "1" if val[tmp[h][0]] == "0" else "0"
            tmp[h][1] = abs(n - tmp[h][1])
            insert(complaints, tmp[h])
            h+=1
        s = convertLsttoStr(val)
        if s in visited and s != main:
            main = s
            k+=1
        else:
            print('a')
            #insert(complaints, current)
            #current = complaints.pop()
        if s not in visited:
            visited.append(s)
    return s

def getComplaints3(preferences, forbiddens, P, M):
    ans = 0

    cnt = 0
    lst = []

    for i in range(P):
        cnt = 0
        for pref in preferences:
            cnt += int(pref[i])
        tple = (i, cnt)
        lst.append(tple)
    i = 0
    j = P - 1
    val = [-1] * P
    n = len(preferences)
    n2 = float((n)/2.0)
    complaints = []
    ans = 0
    while i < P:
        front = lst[i][1]
        if ((n) - front) < n2:
            complaints.append(n - front)
            val[i] = "1"
        else:
            val[i] = "0"
            complaints.append(front)
        i+=1
    main = convertLsttoStr(val)
    s = main
    possible_b = []
    t1 = ("0", complaints[0] if s[0] == "0" else n - complaints[0])
    t2 = ("1", complaints[0] if s[0] == "1" else n - complaints[0])
    insert(possible_b, t1)
    insert(possible_b, t2)
    p = 1
    weigth = [] 
    while p < P:
        i = 0
        l = len(possible_b)
        prev = ''
        tmp = []
        while i < l:
            t1 = (possible_b[i][0]+"0", possible_b[i][1] + (complaints[p] if main[p] == "0" else n - complaints[p]))
            t2 = (possible_b[i][0]+"1", possible_b[i][1] + (complaints[p] if main[p] == "1" else n - complaints[p]))
            insert(tmp, t1)
            insert(tmp, t2)
            i+=1
        m = 0
        possible_b = []
        while m < M + 1 and len(tmp):
            possible_b.append(tmp.pop(0))
            m += 1
        p+=1
    ans = possible_b.pop(0)
    while ans[0] in forbiddens:
        ans = possible_b.pop(0)
        
    return ans[1]

dir = os.path.dirname(__file__)
inp = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())


for case in range(t):

    three_args = list(map(int, inp.readline().split()))

    n = three_args[0]
    m = three_args[1]
    p = three_args[2]

    binary_s = []
    for _ in range(n):
        #binary_s.append("0"*p)
        binary_s.append(inp.readline().strip())
    
    forbidden_s = []
    for _ in range(m):
        #forbidden_s.append("0"*p)
        forbidden_s.append(inp.readline().strip())
    #ans = getComplaints2(binary_s, forbidden_s, p)
    ans = getComplaints3(binary_s, forbidden_s, p, m)
    result = int(out.readline().split(':')[1])
    if result != ans:
        print(('Case #%d: ERROR') % (case+1))
        ans = getComplaints3(binary_s, forbidden_s, p, m)
    case =('Case #%d: %s') % (case+1, ans)
    
    print(case)

print("--- %s seconds ---" % (time.time() - start_time))