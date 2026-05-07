class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Time: O(m * n)
        Space: O(m * n)

        '''
        m = len(s1)
        n = len(s2)

        if len(s3) != m + n: return False

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True # We can create "" using no characters from s1 and s2

        for i in range(1, m + 1):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]
        
        for j in range(1, n + 1):
            dp[0][j] = s2[j - 1] == s3[j - 1] and dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1 # idx of s3 to look at

                # Can check to either consider including i or include j
                include_i = s1[i - 1] == s3[k] and dp[i - 1][j]
                include_j = s2[j - 1] == s3[k] and dp[i][j - 1]

                dp[i][j] = include_i or include_j

        return dp[m][n]
        
