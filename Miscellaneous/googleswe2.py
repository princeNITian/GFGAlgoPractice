import sys


# Time Complexity = max( O(M*N) , O(Q*M) ) = O(M*N), Space Complexity = O(M*N)
def match_count(words,queries):
    
    res = []
    
    lookup = [{} for i in range(len(words[0]))]
    
    # Time complexity for this loop is O(M*N)
    
    for i in range(len(words[0])): #O(M)
        for x in words:			   #O(N)
            if lookup[i].get(x[i]):#O(1)
                lookup[i][x[i]] += 1 
            else:
                lookup[i][x[i]] = 1 
    
    # Time complexity for this loop is O(Q*M)
    for q in queries:				#O(Q)
        count = sys.maxsize
        for j in range(len(q)):		#O(M)
            if lookup[j].get(q[j]): #O(1)
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