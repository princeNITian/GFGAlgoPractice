from collections import defaultdict
class Solution:
    def __init__(self):
        self.result = set()
        self.trie = Trie()

    def findWords(self,board: 'List[List[str]]',words: 'List[str]')->'List[str]':
        for word in words:
            self.trie.insert(word)

        m = len(board)
        n = len(board[0])

        # keep track of letter already visited.
        visited = [[False for i in range(n)] for j in range(m)] 

        for row in range(m):
            for col in range(n):
                self.dfs(board,visited,"",row,col,self.trie)

        return [word for word in self.result] #list(self.result)


    def dfs(self,board,visited,s,row,col,trie):

        if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
            return

        s += board[row][col]
        if not trie.startsWith(s):
            return

        if trie.search(s) == True:
            self.result.add(s)

        visited[row][col] = True #Mark the letter as visited

        self.dfs(board,visited,s,row+1,col,trie) # Down
        self.dfs(board,visited,s,row-1,col,trie) # Up
        self.dfs(board,visited,s,row,col+1,trie) # Right
        self.dfs(board,visited,s,row,col-1,trie) #Left

        visited[row][col] = False

        # Time O(row col / AVG length of each word)

class Trie:

    def __init__(self):
        """
        Initialize data structure here
        """
        self.root = TrieNode()

    def insert(self,word: 'str')->'None':
        """
        Insert a word into the trie
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.isword = True

    def search(self,word:'str')->'bool':
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.isword

    def startsWith(self,prefix: 'str')->'bool':
        """
        Returns if there is any word n the trie that starts with the given prefix
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
class TrieNode:
    def __init__(self):
        self.isword = False
        self.children = defaultdict(TrieNode)

if __name__=="__main__":
    board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ]
    words = ["oath","pea","eat","rain"]

    sol = Solution()
    res = sol.findWords(board,words)
    print(res)