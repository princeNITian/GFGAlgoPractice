import sys

def match_count(words,queries):
    
    res = []
    
    lookup = [{} for i in range(len(words[0]))]
    
    for i in range(len(words[0])):
        for x in words:
            if x[i] in lookup[i]:
                lookup[i][x[i]] += 1 
            else:
                lookup[i][x[i]] = 1 
    
    for q in queries:
        count = sys.maxsize
        for j in range(len(q)):
            if q[j] in lookup[j]:
                count = min(count,lookup[j][q[j]])
            else:
                pass
        res.append(count)
        
    return res

if __name__=="__main__":
    MN = list(map(int,input().split()))
    M = MN[0]
    N = MN[1]
    words = []
    for i in range(M):
        words.append(input())
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input())
    res = match_count(words,queries)
    
    for x in res:
        print(x)
    
    