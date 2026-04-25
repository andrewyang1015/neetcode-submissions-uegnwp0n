from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dag = defaultdict(list)
        n = len(words)
        

        characters = set()
        for word in words:
            for letter in word:
                characters.add(letter)
        
        in_degree = {char: 0 for char in characters}

        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]

            ptr1, ptr2 = 0, 0

            while ptr1 < len(word1) and ptr2 < len(word2):
                if word1[ptr1] == word2[ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    # Found information, move on to next word
                    dag[word1[ptr1]].append(word2[ptr2])
                    in_degree[word2[ptr2]] += 1
                    break
            
            # Word 2 is a substring of word 1, not possible ordering at all
            if ptr1 < len(word1) and ptr2 == len(word2): return ""
            
        
        queue = deque()
        for char in characters:
            if in_degree[char] == 0: queue.append(char)
        
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for adj in dag[char]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
        
        if len(order) != len(characters): return ""

        return "".join(order)
        
