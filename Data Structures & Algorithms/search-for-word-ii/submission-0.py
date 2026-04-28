class TrieNode:
    def __init__(self):
        self.children = [None]* 26
        self.isEnd = False
    
    def insert(self, word):
        cur = self
        for letter in word:
            idx = ord(letter) - ord('a')
            if cur.children[idx] is None: cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = TrieNode()
        for word in words: trie.insert(word)

        valid = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, parent, word):
            temp = board[i][j]
            board[i][j] = "#"

            idx_parent = ord(temp) - ord('a')

            node = parent.children[idx_parent]

            if node.isEnd:
                valid.append(word)
                node.isEnd = False # mark so we don't revisit
            
            for x, y in directions:
                new_r, new_c = i + x, j + y

                if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] != '#':
                    char = board[new_r][new_c]
                    idx = ord(char) - ord('a')

                    if node.children[idx]: dfs(new_r, new_c, node, word + char)

            # Prune node if leaf
            if all(children is None for children in node.children):
                parent.children[idx_parent] = None


            board[i][j] = temp

        

        for i in range(m):
            for j in range(n):
                idx = ord(board[i][j]) - ord('a')
                if trie.children[idx]: dfs(i, j, trie, board[i][j])
        
        return valid
