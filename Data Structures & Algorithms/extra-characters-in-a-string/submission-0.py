class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def insert(self, word):
        cur = self
        for letter in word:
            idx = ord(letter) - ord('a')
            if cur.children[idx] is None: cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True
    
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        trie = TrieNode()
        for word in dictionary: trie.insert(word)

        dp = [n - i for i in range(n + 1)]
        
        for start_idx in range(n - 1, -1, -1):
            optimal = dp[start_idx + 1] + 1
            node = trie

            for end_idx in range(start_idx, n):
                letter = s[end_idx]
                trie_idx = ord(letter) - ord('a')

                if node.children[trie_idx] is None:
                    break

                node = node.children[trie_idx]

                # At an end means we have a word, so see if this allows us to get a
                # smaller minimum
                if node.isEnd:
                    optimal = min(optimal, dp[end_idx + 1])
            
            dp[start_idx] = optimal
        
        return dp[0]

        