from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.isword = False
        self.children = defaultdict(TrieNode)
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.isword = True
        
    def search(self,word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.isword
        
    def startsWith(self,prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
        
if __name__=="__main__":
    t = Trie()
    words = ['cat','car','mat','map','cow']
    for word in words:
        t.insert(word)
    print(t.startsWith('co'))
    print(t.search('car'))
    